from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Auctions(models.Model):
    pass

class Listings(models.Model):
    FASHION = 'FS'
    TOYS = 'TY'
    ELECTRONICS = 'EE'
    HOME = 'HM'
    GARDEN = 'GR'
    CATEGORY_CHOICES = [
        (FASHION, 'Fashion'),
        (TOYS, 'Toys'),
        (ELECTRONICS, 'Electronics'),
        (HOME, 'Home'),
        (GARDEN, 'Garden'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    image = models.URLField(default=None)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=ELECTRONICS,
    )
    starting_bid = models.IntegerField(default=5.00)
    published = models.DateField(auto_now_add=False)
    description = models.TextField(max_length=256)
    ended = models.BooleanField(default=None)
    watchlist = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} {self.title} {self.published}"


class Bids(models.Model):
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    previous = models.IntegerField()
    current = models.IntegerField()
    starting = models.IntegerField()

    def __str__(self):
        return f"{self.current} {self.starting}"

class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.DateTimeField( auto_now_add=True)
    message = models.TextField(max_length=256)

    def __str__(self):
        return f"{self.author} {self.published} {self.message}"
