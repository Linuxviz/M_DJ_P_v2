from django.contrib import admin
from .models import Actor, Category, Rating, RatingStar, Movie, MovieShots, Genre, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "title")
    list_display_links = ("title",)


class ReviewInline(admin.TabularInline):
    readonly_fields = ('email', 'name')
    model = Review
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__title")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    #fields = (("actors", "directors", "genre"),)
    fieldsets = (
        (
            None, {
                "fields": (("title", "tagline"),)
            }
        ),
        (),
        (),
        (),
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("email", "name")


admin.site.register(Actor)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots)
admin.site.register(Genre)
admin.site.register(Review, ReviewAdmin)
