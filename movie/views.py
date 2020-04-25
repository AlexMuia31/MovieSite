from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks

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

    def get_object(self):
        object=super(MovieDetail,self).get_object()
        object.views_count +=1
        object.save()
        return object


    def get_context_data(self, **kwargs):
        context= super(MovieDetail, self).get_context_data(**kwargs)
        context['links']= MovieLinks.objects.filter(movie=self.get_object())
        return context
    
class MovieCategory(ListView):
    model = Movie
    paginate_by = 1
    
    def get_queryset(self):
        self.category= self.kwargs['category']
        
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context= super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']=self.category
        return context

        
