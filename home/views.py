from django.shortcuts import render, redirect,\
    get_object_or_404, reverse
from django.contrib import messages
from .forms import ContactForm
from products.models import Product, Category
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


def home(request):
    """ VIEW TO RETURN HOME """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            # categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "Your search is invalid")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
        # 'current_categories': categories
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
