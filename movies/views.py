from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Movie
from .forms import ReviewForm


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


class AddReviewView(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
