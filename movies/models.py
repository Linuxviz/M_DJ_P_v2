from django.db import models
from datetime import date


# Create your models here.

class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=40)
    description = models.TextField(verbose_name="Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Movie(models.Model):
    title = models.CharField(verbose_name="Название фильма", max_length=200)
    tagline = models.CharField(verbose_name="Слоган", max_length=200, default='')
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(verbose_name="Постер", upload_to='movie/')
    year = models.SmallIntegerField(verbose_name="Год съёмки")
    country = models.CharField(verbose_name="Страна", max_length=100)
    director = models.ManyToManyField('Actor', verbose_name="Режиссёры", related_name='movie_director')
    actors = models.ManyToManyField('Actor', verbose_name="Актёры", related_name='movie_actors')
    genre = models.ManyToManyField('Genre', verbose_name="Жанр")
    world_primer = models.DateField(verbose_name="Премьера в мире")
    budget = models.PositiveIntegerField(verbose_name="Бюджет", default=0, help_text="В доллорах США")
    fees_in_usa = models.PositiveIntegerField(verbose_name="Сборы в США", default=0, help_text="В долларах США")
    fees_in_world = models.PositiveIntegerField(verbose_name="Сборы в мире", default=0, help_text="В долларах США")
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(verbose_name="Черновик", default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Actor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='actors/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Актёры и режисёры'
        verbose_name_plural = 'Актёры и режисёры'


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=150)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Review(models.Model):
    email = models.EmailField(verbose_name="Электронная почта")
    name = models.CharField(verbose_name="Имя", max_length=150)
    text = models.TextField(verbose_name="Отзыв", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey('Movie', verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"отзыв {self.name} к фильму {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rating(models.Model):
    ip = models.CharField(verbose_name="IP адрес", max_length=15)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name="Звезда")
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name="Фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class RatingStar(models.Model):
    value = models.SmallIntegerField(verbose_name="Звезды рейтинга", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class MovieShots(models.Model):
    title = models.CharField(verbose_name="Название", max_length=150)
    description = models.TextField(verbose_name="Описание", default='')
    image = models.ImageField(verbose_name="Фото", upload_to="movie_shots/")
    id_movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"
