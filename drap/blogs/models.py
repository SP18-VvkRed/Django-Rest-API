from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=500,blank=False, default='')
    author = models.CharField(max_length=30, blank=False,  default='Anonymous')
    published = models.BooleanField(default=False)