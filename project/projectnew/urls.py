from django.contrib import admin
from django.urls import path
from.views import contact

urlpatterns = [
    path('contact/', contact, name = 'Contact'),
]