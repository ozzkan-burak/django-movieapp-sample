from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the movies index page.")

def movies(request):
    return HttpResponse("Hello, world. You're at the movies page.")

def movie_details(request, slug):
    return HttpResponse("Hello, world. You're at the " + slug + " movie details page.")
