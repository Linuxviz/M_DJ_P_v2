from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Actor, Category, Rating, RatingStar, Movie, MovieShots, Genre, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "title")
    list_display_links = ("title",)


class ReviewInline(admin.TabularInline):
    """Отзывы на админ. странице фильмов"""
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
    # fields = (("actors", "directors", "genre"),)
    fieldsets = (
        (
            None, {
                "fields": (("title", "tagline"),)
            }
        ),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Действующие лица", {
            "classes": ("collapse",),
            "fields": (("actors", "director", "genre", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Служебные поля", {
            "fields": (("url", "draft"),)
        }),
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("email", "name")


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url")


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip")


class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "id_movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingStar)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
