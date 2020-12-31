from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_listing, name="new"),
    # path("active", views.active_listings, name="active_listings"),
    # path("categories", views.categories, name="categories"),
    # path("watchlist", views.watchlist, name="watchlist")

]
