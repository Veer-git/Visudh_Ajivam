from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("business_registration", views.business_registration, name="business_registration"),
    path("business_login", views.business_login, name="business_login"),
]
