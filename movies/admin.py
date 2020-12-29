from django.contrib import admin
from .models import Actor, Category, Rating, RatingStar, Movie, MovieShots, Genre, Review

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Genre)
admin.site.register(Review)
