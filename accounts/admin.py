from django.contrib import admin
from .models import Customer, Product, Order, Tag
# Register your models here.

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ["status",]
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)