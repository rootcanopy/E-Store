from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    """ view to return landing page """
    return render(request, 'home/index.html')


def contact_page(request):
    """ view to return landing page """
    return render(request, 'home/contact.html')


def about_page(request):
    """ view to return landing page """
    return render(request, 'home/about.html')
