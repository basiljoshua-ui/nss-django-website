from django.db import models

class Report(models.Model):

    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='reports/')
    date = models.DateField()

    def __str__(self):
        return self.title