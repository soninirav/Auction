from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category/",views.category,name="category"),
    path("add_to_watchlist/<int:listing_id>/",views.add_to_watchlist,name="add_to_watchlist"),
    path("remove_from_watchlist/<int:listing_id>/",views.remove_from_watchlist,name="remove_from_watchlist"),
    path("watchlist/",views.watchlist,name="watchlist"),
    path("category/<int:id>/",views.category_listing,name="category_listing"),
    path("listing/create/",views.create,name="create_listing"),
    path("listing/<int:listing_id>",views.detail,name="detail_listing"),
    path("listing/<int:listing_id>/close/",views.close_listing,name="close_listing"),

]
