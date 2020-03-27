from django.shortcuts import render, redirect
from .models import Surl, encode, decode
from urllib.parse import urlparse

def index(request):
    if request.method == 'POST':
        if urlparse(request.POST['url']).scheme == '':
            url = 'http://' + request.POST['url']
        else:
            url = request.POST['url']
        try:
            id = Surl.objects.get(url=url).id
            return render(request, "index.html", {"short_url": 'http://localhost:8000/'+encode(id)})
        except Surl.DoesNotExist:
            surl = Surl(url=url)
            surl.save()
            return render(request, "index.html", {"short_url": 'http://localhost:8000/'+encode(surl.id)})
    else:
        print(request.method)
        print('blya')
        return render(request, "index.html")
