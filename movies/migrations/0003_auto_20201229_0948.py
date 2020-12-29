# Generated by Django 3.1.4 on 2020-12-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201229_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='url',
            field=models.SlugField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
