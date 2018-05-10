# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello2(request):
    html = "<html><body>Hello 2nd app</body></html>"
    return HttpResponse(html)
