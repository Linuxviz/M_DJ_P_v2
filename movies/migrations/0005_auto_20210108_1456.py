# Generated by Django 3.1.4 on 2021-01-08 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210103_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='world_primer',
            new_name='world_premiere',
        ),
    ]