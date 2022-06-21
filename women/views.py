from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("Страница приложения women")

def categories(request, cat): #HttpRequest
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>") 


