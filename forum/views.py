# -*- coding:utf-8 -*-

from djangp.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")