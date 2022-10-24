from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def hello(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()~'))

    length = int(request.GET.get('length', 12))
    the_password = ''
    for x in range(length):
        the_password += random.choice(chars)
    return render(request, 'generator/password.html', {'password': the_password})

def info(request):
    return render(request, 'generator/info.html')