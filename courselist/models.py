from django.db import models

# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)