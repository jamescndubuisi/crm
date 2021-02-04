from django.shortcuts import render, redirect
from .models import Product,Customer, Order
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
# Create your views here.


def homepage(request):
    title = "Home page"
    orders = Order.objects.all()
    customers = Customer.objects.all()
    product = Product.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="Pending").count()
    context = {"orders":orders,"customers": customers,"products":product,"title":title,"customer_count":total_customers,"order_count":total_orders,"pending":orders_pending,"delivered":delivered}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    title = "Products"
    product_list = Product.objects.all()
    context =  {"title":title,"products":product_list}
    return render(request,'accounts/products.html',context)


def customer_data(request,pk):
    title = "Customers"
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {"title":title,"customer":customer,"orders":orders,"order_filter":my_filter,"order_count":order_count}
    return render(request,'accounts/customer.html',context )

def customer_list(request):
    title = "Customers"
    customer = Customer.objects.all()
    context = {"title":title,"customer":customer}
    return render(request,'accounts/customer.html',context )

def create_order(request, pk):
    orderformset = inlineformset_factory(Customer,Order,fields=('product',"status"), extra=5)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={"customer":customer})
    formset = orderformset(queryset=Order.objects.none(),instance=customer)
    context={"formset":formset}
    if request.method=="POST":
        print(request.POST)
        formset=orderformset(request.POST, instance=customer)
        if formset.is_valid():
            print("saving")
            formset.save()
            return redirect("home")
        else:
            print("wahala")
    return render(request, "accounts/order_form.html", context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context={"form":form}
    if request.method=="POST":
        print(request.POST)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "accounts/order_form.html", context)



def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    context={"item":order}
    if request.method=="POST":
        order.delete()
        return  redirect("home")

    return render(request, "accounts/delete.html", context)



