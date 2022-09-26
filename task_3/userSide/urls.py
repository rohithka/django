# connecting userSide with views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name = "user_home"),
    path("shop/", views.Shop.as_view(), name = "user_shop")
]