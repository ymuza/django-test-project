from django.shortcuts import render
from watchlist_app.models import Movie
# Create your views here.

class movies:
    
    
    def movie_list(request):
        movies = Movie.objects.all()
        