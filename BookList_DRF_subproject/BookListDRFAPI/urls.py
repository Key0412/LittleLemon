from django.urls import path
from .views import book

urlpatterns = [
    path('books/', book)
]