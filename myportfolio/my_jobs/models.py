from django.db import models

# Create your models here.

class my_job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 200)
