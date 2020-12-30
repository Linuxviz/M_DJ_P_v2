from django.shortcuts import render
from django.views.generic import View
from .models import Movie


def main_test(request):
    return render(request, template_name='movies/main.html')


class HomePageView(View):
    "Список фильмов"

    def get(self, request):
        movies = Movie.objects.all()
        return render(request=request, template_name='movies/movies.html', context={'movie_list': movies})
