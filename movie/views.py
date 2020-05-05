from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks
from django.views.generic.dates import YearArchiveView

class MovieList(ListView):
    model= Movie
    #object_context_name =''
    #template_name=''
    context_object_name = 'movies'  # Default: object_list
    paginate_by = 10
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
        context['related_movies']= Movie.objects.filter(category=self.get_object().category)#.order_by['created'][0:6]

        return context
    
class MovieCategory(ListView):
    model = Movie
    paginate_by = 10
    
    def get_queryset(self):
        self.category= self.kwargs['category']
        
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context= super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']=self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    paginate_by = 10
    
    def get_queryset(self):
        self.language= self.kwargs['language']
        
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context= super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_langauge']=self.language
        return context

class MovieSearch(ListView):
    model= Movie
    paginate_by= 10

    def get_queryset(self):
        query= self.request.GET.get('query')
        if query:
            object_list= self.model.objects.filter(title__icontains=query)
            
        else:
            object_list=self.model.objects.none()

        return object_list

class MovieYear(YearArchiveView):
    queryset= Movie.objects.all()
    date_field='year_of_production'
    make_object_list= True
    allow_future= True


class HomeView(ListView):
    model= Movie
    template_name= 'home.html'

    def get_context_data(self, **kwargs):
        context= super(HomeView,self).get_context_data(**kwargs)
        context['top_rated']=Movie.objects.filter(category='TR')
        context['most_watched']=Movie.objects.filter(category='MW')
        context['recently_added']=Movie.objects.filter(category='RA')
        return context
        
