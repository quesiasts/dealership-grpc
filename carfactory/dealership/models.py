from django.db import models

class Car(models.Model):

    brand = models.CharField(max_length=100)
    release_year = models.DateField()
    color = models.CharField(max_length=6, default='black')

    class Meta:
        ordering = ['brand']

