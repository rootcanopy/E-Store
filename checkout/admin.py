from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = (
        'orderitem_total',
    )

class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemAdminInline,
    )
    readonly_fields = (
        'order_id', 'date',
        'delivery_cost', 'order_total',
        'grand_total',
    )
    field = (
        'order_id', 'date',
        'full_name', 'email',
        'phone_number', 'country',
        'postcode', 'town_or_city',
        'address', 'address2',
        'county', 'delivery_cost',
        'order_total', 'grand_total',
    )
    list_display = (
        'order_id', 'date',
        'full_name', 'delivery_cost',
        'order_total', 'grand_total',
    )
    ordering = (
        '-date',
    )

admin.site.register(Order, OrderAdmin)
