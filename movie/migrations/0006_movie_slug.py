# Generated by Django 2.2.10 on 2020-04-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200426_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
