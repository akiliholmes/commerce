from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm

from .models import *

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'image', 'description', 'startingBid']

class NewBidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['newBid']

class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['title']
            image = form.cleaned_data['image']
            starting_bid = form.cleaned_data['starting_bid']
            cc_myself = form.cleaned_data['description']

            # save_f(title, image, starting_bid, description)

            return HttpResponseRedirect(reverse("active_listings"))
        else:
            return render(request, "auctions/new.html",{
                "form": form
            })
    else:
        return render(request, "auctions/new.html",{
            "form": NewListingForm()
        })


# def active_listings(request):


# def categories(request):


# def watchlist(request):
