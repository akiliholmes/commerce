from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images/")
    published = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=256)
    currentBid = models.FloatField(blank=True, null=True)
    startingBid = models.FloatField()
    ended = models.BooleanField(default=False)
    watchlist = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, )

    def __str__(self):
        return f"{self.title} {self.currentBid}"


class Bid(models.Model):
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    previousBid = models.IntegerField()
    currentBid = models.IntegerField()
    newBid = models.IntegerField()

    def __str__(self):
        return f"{self.currentBid}"

class Comment(models.Model):
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.message}"
