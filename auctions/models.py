from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(AbstractUser):
    pass

class Auctions(models.Model):
    pass

class Listings(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.URLField(default=None)
    starting_bid = models.IntegerField(default=5.00)
    published = models.DateField()
    description = models.TextField(max_length=256)
    watchlist = models.BooleanField(default=False)
    ended = models.BooleanField(default=None)

    def __str__(self):
        return f"{self.author} {self.title} {self.published}"


class Bids(models.Model):
    previous = models.IntegerField()
    current = models.IntegerField()
    starting = models.IntegerField()

    def __str__(self):
        return f"{self.current} {self.starting}"

class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateField()
    message = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.author} {self.published}"
