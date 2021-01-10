from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Actor, Category, Rating, RatingStar, Movie, MovieShots, Genre, Review
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


admin.site.site_title = "Django movie"
admin.site.site_header = "Django movie"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "title")
    list_display_links = ("title",)


class ReviewInline(admin.TabularInline):
    """Отзывы на админ. странице фильмов"""
    readonly_fields = ('email', 'name')
    model = Review
    extra = 1


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="120">')

    get_image.short_description = "Изображение"


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__title")
    inlines = [MovieShotsInLine, ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image",)
    list_editable = ("draft",)
    actions = ['publish', 'unpublish']
    form = MovieAdminForm
    fieldsets = (
        (
            None, {
                "fields": (("title", "tagline"),)
            }
        ),
        (None, {
            "fields": ("description", ("get_image", "poster"))
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

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="500" height="500">')

    get_image.short_description = "изображение"

    def unpublish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "запись обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "запись обновлена"
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change',)


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
