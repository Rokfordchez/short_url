import string
from math import floor
from django.db import models
from url_shortener.settings import ENCODE_BASE, CONST_VAL


class Surl(models.Model):
    url = models.URLField()


def encode(num, b=ENCODE_BASE, const=CONST_VAL):
    num = num + const
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    result = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        result = base[int(r)] + result
    return result


def decode(num, b=ENCODE_BASE, const=CONST_VAL):
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    limit = len(num)
    result = 0
    for i in range(limit):
        result = b * result + base.find(num[i])
    return result - const
