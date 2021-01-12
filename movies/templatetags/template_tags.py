from django import template

from movies.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод категорий фильмов"""
    return Category.objects.all()


@register.inclusion_tag('include/_last_add.html')
def get_last(count=5):
    movie = Movie.objects.order_by("id")[:count]
    return {'last_movies': movie}
