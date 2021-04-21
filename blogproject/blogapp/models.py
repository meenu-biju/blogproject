from django.db import models


# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='picture')
    heading = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    date = models.DateField()
