
from django.urls import path
from .views import MovieDetail, MovieList, MovieCategory, MovieLanguage

app_name= 'movie'

urlpatterns = [
    path('',MovieList.as_view(), name='movie_list' ),
    path('category/<str:category>',MovieCategory.as_view(), name='movie_category'),
    path('language/<str:language>',MovieLanguage.as_view(), name='movie_language'),
    path('<int:pk>',MovieDetail.as_view(), name='movie_detail'),
] 