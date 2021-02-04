from django.urls import path
from . views import homepage,log_in, register, products, customer_data, customer_list, create_order, update_order, delete_order

urlpatterns = [
    path('', homepage, name = "home"),
    path('login/', log_in, name = "login"),
    path('register/', register, name = "register"),
    path('products', products, name = "products"),
    path('customers', customer_list, name = "customers"),
    path('customers/<str:pk>', customer_data, name = "customer_details"),


    path('create_order/<str:pk>/', create_order, name = "create_order"),
    path('update_order/<str:pk>', update_order, name = "update_order"),
    path('delete_order/<str:pk>', delete_order, name = "delete_order"),
]
