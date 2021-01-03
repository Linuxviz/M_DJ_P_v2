from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail')
]
