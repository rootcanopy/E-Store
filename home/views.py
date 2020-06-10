from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def home_page(request):
    """ view to return landing page """
    return render(request, 'home/index.html')


def contact_page(request):
    """ view to return contact page """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

    return render(request, 'home/contact.html')


def about_page(request):
    """ view to return about page """
    return render(request, 'home/about.html')
