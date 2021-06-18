from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.TextField()
    context = models.TextField()
    date = models.DateField()