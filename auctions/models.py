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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="author_list")
    title = models.CharField(max_length=64)
    image = models.URLField()
    published = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_list")
    description = models.TextField(max_length=256)
    startingBid = models.FloatField()
    ended = models.BooleanField(default=False)
    watchlist = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="watch_list")

    def __str__(self):
        return f"{self.title} {self.currentBid}"


class Bid(models.Model):
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    newBid = models.IntegerField()

    def __str__(self):
        return f"{self.newBid}"

class Comment(models.Model):
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=256)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_review")

    def __str__(self):
        return f"{self.message}"
