from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    copyright = models.CharField(max_length=25, blank=True)
    isbn = models.CharField(max_length=25, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    keyword = models.CharField(max_length=50, null=True, blank=True)
    # want to do another model for keywords, manytomany, but will come in later updates
