from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies" : [
        {
            "title": "film adı 1",
            "description": "film açıklama 1",
            "imageUrl": "m1.jpg",
            "slug": "film-adi-1",
            "language": "english",
            "date" : "date(2021,10,10)"
        },
        {
            "title": "film adı 2",
            "description": "film açıklama 2",
            "imageUrl": "m2.jpg",
            "slug": "film-adi-2",
            "language": "english",
            "date": "date(2021,5,10)"
        },
        {
            "title": "film adı 3",
            "description": "film açıklama 3",
            "imageUrl": "m3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": "date(2021,10,8)"
        },
        {
            "title": "film adı 4",
            "description": "film açıklama 4",
            "imageUrl": "m4.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": "date(2021,10,21)"
        }
    ],
    "slider": []
}


def index(request):
    movies = data["movies"]
    return render(request, "index.html", {
        "movies": movies
        })
    # return HttpResponse("index")

def movies(request):
    return render(request, "movies.html")

def movie_details(request, slug):
    return render(request, "movie-details.html", {"slug": slug})
