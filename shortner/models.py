from django.db import models

class Urls(models.Model):
    url = models.CharField(max_length=1000)
    urlid = models.CharField(max_length=10)
# Create your models here.
