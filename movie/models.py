from django.db import models
from django.template.defaultfilters import slugify


CATEGORY_CHOICES=(
    ('action','Action'),
    ('drama','Drama'),
    ('comedy','Comedy'),
    ('romance','Romance')
)

LANGUAGE_CHOICES=(
    ('english','English'),
    ('german','German'),
    ('swahili','Swahili'),
    ('spanish','Spanish')
)

STATUS_CHOICES=(
    ('RA','Recently Added'),
    ('MW','Most Watched'),
    ('TR','Top Rated')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20)
    cast= models.CharField(max_length=100)
    status= models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production= models.DateField()
    views_count= models.IntegerField(default=0)
    movie_trailer= models.URLField()

    slug= models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Movie,self).save(*args,**kwargs)

    

    def __str__(self):
        return self.title


LINK_CHOICES=(
    ('D','DOWNLOAD LINK'),
    ('W','WATCH LINK')
)

class MovieLinks(models.Model):
    movie= models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type= models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie)







