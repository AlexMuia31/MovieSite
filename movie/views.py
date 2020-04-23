from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieList(ListView):
    model= Movie
    #object_context_name =''
    #template_name=''
    context_object_name = 'movies'  # Default: object_list
    paginate_by = 1
    queryset = Movie.objects.all()  # Default: Model.objects.all()


class MovieDetail(DetailView):
    model= Movie
    #template_name=''
