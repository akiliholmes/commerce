from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm

from .models import *

class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'image', 'description', 'starting_bid']

class NewBidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['new_bid']

class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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
        form = NewCommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            #cc_myself = form.cleaned_data['description']
            f = form.save()
            # save_f(title, image, starting_bid, description)

            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/new.html",{
                "form": form
            })
    else:
        return render(request, "auctions/new.html",{
            "form": NewCommentForm()
        })


def detail_view(request, listing_id):
    try:
        listing = get_list_or_404(Listing, pk=listing_id)
        return render(request, 'auctions/detail.html', {'listing': listing})
    except Listing.DoesNotExist:
        return render(request, 'auctions/detail.html', {'error': 'No listing found.'})


# def categories(request):


# def watchlist(request):
