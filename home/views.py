from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.


def home_page(request):
    """ view to return landing page """
    return render(request, 'home/index.html')


# USER QUERY FORM
def contact_page(request):
    """ view to return contact page """
    form = ContactForm(request.POST)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
    # if request.method == "POST":
    return render(request, 'home/contact.html', context)


def about_page(request):
    """ view to return about page """
    return render(request, 'home/about.html')
