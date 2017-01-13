#! /usr/bin/env python
#coding=utf-8
from django.shortcuts import render

def home(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'home.html', context)

def crypto(request):
    return render(request, 'crypto.html', {})