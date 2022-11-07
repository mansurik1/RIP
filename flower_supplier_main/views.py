from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def greeting(request, number):
    return HttpResponse(f'<h1>Добро пожаловать!</h1><p>Номер: {number}</p>')


def hello(request):
    return HttpResponse('Hello World!')


def friendly_404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
