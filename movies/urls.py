from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("filter/", FilterMoviesView.as_view(), name='filter'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", AddReviewView.as_view(), name="add_view"),
    path("director/<str:slug>/", DirectorDetailView.as_view(), name="director")
]
