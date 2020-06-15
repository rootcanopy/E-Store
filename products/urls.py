from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('products/', views.product_details, name='product_details'),
]
