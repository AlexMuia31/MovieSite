from . models import Movie

def slider_movies(request):
    #movies= Movie.objects.all().order_by('created')[0:2]
    movies= Movie.objects.first()
    return {'slider_movie': movies}