from http.client import HTTPResponse
from multiprocessing import context
from pickle import GET
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect

from .models import *


menu = [
    {'title':"О сайте", 'url_name':'about' },
    {'title':"Добавить статью", 'url_name':'add_page' },
    {'title':"Обратная связь", 'url_name':'contact' },
    {'title':"Войти", 'url_name':'login' }
]

#["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
   
    context_sp = {
        'posts' : posts,
        'menu' : menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context_sp)

def about(request):
    return render(request, 'women/about.html', {'menu' : menu,'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавить статью")    

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Войти") 

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    
    if len(posts) == 0:
        raise Http404() 

    context_sp = {
        'posts' : posts,
        'menu' : menu,
        'title': 'Ототбражение по рубрикам',
        'cat_selected': cat_id ,
    }
    return render(request, 'women/index.html', context=context_sp)   

#def index(request): #HttpRequest
    #return HttpResponse("Страница приложения women")

#def categories(request, catid):
 #   if request. POST: 
  #      print(request. POST)

   # return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

#def archive(request, year): 
 #   if int(year) > 2020:
  #      return redirect('home', permanent=True)

   # return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>") 

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')