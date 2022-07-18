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
    "sliders": [
        {
            "imageUrl": "slider1.jpg",
            "name": "slider1",
            "url":"film-adi-1",
        },
        {
            "imageUrl": "slider2.jpg",
            "name": "slider2",
            "url": "film-adi-2",
        },
        {
            "imageUrl": "slider3.jpg",
            "name": "slider3",
            "url": "film-adi-3",
        }
    ]
}


def index(request):
    movies = data["movies"][-4:]
    sliders=data["sliders"]
    return render(request, "index.html", {
        "movies": movies,
        "sliders":sliders
        })
    # return HttpResponse("index")

def movies(request):
    movies = data["movies"]
    return render(request, "movies.html",{
        "movies": movies
    })

def movie_details(request, slug):
    return render(request, "movie-details.html", {"slug": slug})
