from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    # return HttpResponse("index")

def movies(request):
    return render(request, "movies.html")

def movie_details(request, slug):
    return render(request, "movie-details.html", {"slug": slug})
