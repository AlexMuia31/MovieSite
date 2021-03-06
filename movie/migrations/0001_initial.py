# Generated by Django 2.2.3 on 2020-04-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='movies')),
                ('category', models.CharField(choices=[('A', 'Action'), ('D', 'Drama'), ('C', 'Comedy'), ('R', 'Romance')], max_length=1)),
                ('language', models.CharField(choices=[('En', 'English'), ('Gr', 'German'), ('Ki', 'Swahili'), ('Sp', 'Spanish')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'Recently Added'), ('MW', 'Most Watched'), ('TR', 'Top Rated')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('views_count', models.TextField(default=0)),
            ],
        ),
    ]
