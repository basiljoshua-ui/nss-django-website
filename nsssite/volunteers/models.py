from django.db import models

class Volunteer(models.Model):

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='volunteers/')
    hours_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.name