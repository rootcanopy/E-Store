from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('<slug:category_slug>/',
    #     views.home_page, name='products_by_category'),
    path('contact/', views.contact_page, name='contact'),
    # path('success/', views.confirm_success, name='success'),
    path('about/', views.about_page, name='about'),
]
