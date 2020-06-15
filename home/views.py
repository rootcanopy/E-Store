from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from products.models import Category, Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def home(request):
    """ VIEW TO RETURN HOME """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)


def home_page(request, category_slug=None):
    """ view to return products on landing page """
    category_page = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category_page = get_object_or_404(
            Category,
            slug=category_slug
        )
        products = Product.objects.filter(category=category_page)
    else:
        products = Product.objects.all().filter(in_stock=True)
    context = {
        'category': category_page,
        'products': products
    }
    return render(request, 'home/index.html', context)


# USER QUERY FORM
def contact_page(request):
    """ view to return contact page """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email_from']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(form.cleaned_data)
            try:
                send_mail(name, subject, message, email_from, ['admin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, f'We have recieved your message and will \
                get back to you as soon as we can!')
            return render(request, 'home/index.html')
        else:
            form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


# REDIRECTS TO A NEW PAGE, WILL NEED TO CHANGE THIS
# def confirm_success(request):
#    return HttpResponse('Success! Thank you for your message.')


# COMPANY ABOUT PAGE
def about_page(request):
    """ view to return about page """
    return render(request, 'home/about.html')
