#! /usr/bin/env python
#coding=utf-8
from django.shortcuts import render
# from django.views.decorators.clickjacking import xframe_options_deny
# from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def home(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'home.html', context)

@xframe_options_exempt
def crypto(request):
    return render(request, 'crypto.html', {})