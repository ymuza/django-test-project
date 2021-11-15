from django.urls import path
from watchlist_app.views import movies

urlpatterns = [
    path('list/', movies.movie_list, name='movie_list'),
]   