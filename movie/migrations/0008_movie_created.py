# Generated by Django 2.2.10 on 2020-05-02 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
