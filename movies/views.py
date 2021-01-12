from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Movie, Category, Actor
from .forms import ReviewForm


class HomePageView(ListView):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(DetailView):
    """Подробности о фильме"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class DirectorDetailView(DetailView):
    """Подробности о фильме"""

    model = Actor
    slug_field = "name"
    template_name = "movies/directors.html"


class AddReviewView(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent", None))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
