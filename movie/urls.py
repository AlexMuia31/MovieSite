
from django.urls import path
from .views import MovieDetail, MovieList, MovieCategory, MovieLanguage,  MovieSearch, MovieYear, HomeView

app_name= 'movie'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('',MovieList.as_view(), name='movie_list' ),
    path('category/<str:category>',MovieCategory.as_view(), name='movie_category'),
    path('language/<str:language>',MovieLanguage.as_view(), name='movie_language'),
    path('search/',MovieSearch.as_view(), name='movie_search'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
    path('<slug:slug>',MovieDetail.as_view(), name='movie_detail'),
] 