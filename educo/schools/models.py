from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    img_link = models.CharField(max_length=5000)
    web_link = models.CharField(max_length=5000)