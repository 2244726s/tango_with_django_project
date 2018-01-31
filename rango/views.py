from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def show_category(request, category_name_slug):
    context_dict = {}


    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        #don't do anything
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'content': 'This tutorial has been put together by Jonathan Sprague'}
    return render(request, 'rango/about.html', context=context_dict)