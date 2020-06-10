from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def home_page(request):
    """ view to return landing page """
    return render(request, 'home/index.html')


# USER QUERY FORM
def contact_page(request):
    """ view to return contact page """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(form.cleaned_data)
            try:
                send_mail(subject, message, email, ['admin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'home/contact.html', {'form': form})


# REDIRECTS TO A NEW PAGE, WILL NEED TO CHANGE THIS
def confirm_success(request):
    return HttpResponse('Success! Thank you for your message.')


# COMPANY ABOUT PAGE
def about_page(request):
    """ view to return about page """
    return render(request, 'home/about.html')
