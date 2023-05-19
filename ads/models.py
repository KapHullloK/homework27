from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=25)
    price = models.IntegerField()
    description = models.CharField(max_length=2500)
    address = models.CharField(max_length=250)
    is_published = models.CharField(max_length=10)

