from django.db import models


CATEGORY_CHOICES=(
    ('A','Action'),
    ('D','Drama'),
    ('C','Comedy'),
    ('R','Romance')
)

LANGUAGE_CHOICES=(
    ('En','English'),
    ('Gr','German'),
    ('Ki','Swahili'),
    ('Sp','Spanish')
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
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status= models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production= models.DateField()
    views_count= models.IntegerField(default=0)

    def __str__(self):
        return self.title


