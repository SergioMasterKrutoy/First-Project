from django.urls import path
from .views import *

urlpatterns = [
    path('', YAP_rating, name='index'),
]