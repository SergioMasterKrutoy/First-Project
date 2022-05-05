from django.shortcuts import render
from .models import YAP_rating
def YAP_rating(request):
    return render(request, 'index.html')

