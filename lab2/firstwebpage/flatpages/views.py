from django.shortcuts import render
from django.http import HttpResponse
from django import template

def home(request):
    # return HttpResponse(
    #     u'Вариант 17. Система учета внутриофисных расходов',
    #     content_type="text/html; charset=utf-8"
    # )
     return render(request, 'static_handler.html')


