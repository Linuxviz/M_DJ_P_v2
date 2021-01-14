from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Movie, Category, Actor, Genre, Rating
from .forms import ReviewForm, RatingForm


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class HomePageView(ListView, GenreYear):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(DetailView, GenreYear):
    """Подробности о фильме"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class DirectorDetailView(DetailView, GenreYear):
    """Подробности о фильме"""

    model = Actor
    slug_field = "name"
    template_name = "movies/actors_and_directors_detail.html"


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


class FilterMoviesView(GenreYear, ListView):
    template_name = 'movies/movies.html'

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(genre__in=self.request.GET.getlist("genre")) |
            Q(year__in=self.request.GET.getlist("year"))
        ).distinct()
        return queryset


class AddStarRating(View):
    """Добавление рейтинга к фильму"""

    def get_client_ip(self, request):
        x_forwarder_for = request.META.get('HTTP_X_FORWARDER_FOR')
        if x_forwarder_for:
            ip = x_forwarder_for.split(',')[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
