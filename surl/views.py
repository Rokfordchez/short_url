import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Surl, encode, decode
from urllib.parse import urlparse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    response_data = dict()
    response_data['message'] = ''
    if request.POST.get('action') == 'post' and request.POST['url'] != '':
        if urlparse(request.POST['url']).scheme == '':
            url = 'http://' + request.POST['url']
        else:
            url = request.POST['url']
        try:
            id = Surl.objects.get(url=url).id
            response_data['short_url'] = 'http://localhost:8000/' + encode(id)
            return JsonResponse(response_data)
        except Surl.DoesNotExist:
            try:
                r = requests.get(url, timeout=3)
            except requests.exceptions.ConnectTimeout:
                response_data['message'] = 'incorrect url'
                return JsonResponse(response_data)
            if r.status_code == 200:
                surl = Surl(url=url)
                surl.save()
                response_data['short_url'] = 'http://localhost:8000/' + encode(surl.id)
                return JsonResponse(response_data)
            else:
                response_data['message'] = 'incorrect url'
                return JsonResponse(response_data)
    return render(request, "index.html")


def go_to_url(request, path):
    id = decode(request.path[1:])
    try:
        url = Surl.objects.get(id=id).url
        return HttpResponseRedirect(url)
    except Surl.DoesNotExist:
        return render(request, "index.html")
