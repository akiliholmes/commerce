from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new-listing", views.new_listing, name="new_listing"),
    path("<int:listing_id>", views.listing_details, name="listing_details"),
    path("categories", views.all_categories, name="categories"),
    # path("<str:categories>", views.categories_names, name="categories_"),
    path("watchlist", views.watchlist, name="watchlist")

]
