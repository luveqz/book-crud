from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=100)
