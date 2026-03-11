from django.db import models

class Event(models.Model):

    CATEGORY_CHOICES = [
        ('environment','Environmental'),
        ('health','Health Camp'),
        ('social','Social Awareness'),
        ('special','Special Camp'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    date = models.DateField()
    cover_image = models.ImageField(upload_to='events/')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title