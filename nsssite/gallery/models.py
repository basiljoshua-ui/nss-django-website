from django.db import models

class Album(models.Model):

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    event = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='gallery/covers')

    def __str__(self):
        return self.title


class Image(models.Model):

    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/images')
    caption = models.CharField(max_length=200,blank=True)