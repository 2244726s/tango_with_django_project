from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'content': 'This tutorial has been put together by Jonathan Sprague'}
    return render(request, 'rango/about.html', context=context_dict)