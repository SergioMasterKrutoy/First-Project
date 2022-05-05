from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("This is my page")


def home(request):
    return render(request, 'home.html',
                  {'greeting': 'Hello'})

def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    text_area = len(user_text.split())
    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reverse_text': reverse_text,
                  'text_area': text_area})