from django.contrib import admin
from .models import Product, Category, Customer_orders, OrderItems

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer_orders)
admin.site.register(OrderItems)