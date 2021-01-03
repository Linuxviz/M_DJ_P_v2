from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


def main_test(request):
    return render(request, template_name='movies/main.html')


class HomePageView(ListView):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    """Подробности о фильме"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

