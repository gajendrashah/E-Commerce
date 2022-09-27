import re
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .form import OrderCreationForm, ProductCreationForm
from userapp.models import Customers, Orders, Product, ProductImage

def index(request):

    return render(request,"adminapp/index.html")



def sales(request):

    return render(request,"adminapp/index.html")


def purchase(request):

    return render(request,"adminapp/index.html")


    
def expence(request):

    return render(request,"adminapp/index.html")

def payment(request):

    return render(request,"adminapp/index.html")


def daybook(request):

    return render(request,"adminapp/index.html")


def ledger(request):

    return render(request,"adminapp/index.html")


def finalaccount(request):

    return render(request,"adminapp/index.html")



def customer(request):

    return render(request,"adminapp/index.html")
def supplier(request):

    return render(request,"adminapp/index.html")


def product(request):
    product = Product.objects.all()
    form = ProductCreationForm
    
    
    if request.method == 'POST':
        form = ProductCreationForm(request.POST ,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            return HttpResponse("file cant upload")

    
    context= {"form":form,"product":product}
    return render(request,"adminapp/product.html",context)


def product_update(request,pk):
    order = get_object_or_404(Product,id=pk)
    form = ProductCreationForm(instance=order)
    if request.method == 'POST':
        print(request.POST)
        form = ProductCreationForm(request.POST, request.FILES,instance=order)
        if form.is_valid():
            form.save()
        return redirect('product')
    context = {'form':form}
    return render (request,"adminapp/product_update.html",context)


def product_delete(request,pk):
    print(pk)
    order = get_object_or_404(Product,id=pk)
    # if request.method == "POST":
    order.delete()
    return redirect('product')

	



def setting(request):

    return render(request,"adminapp/index.html")



def order(request):

    order = Orders.objects.all()
    form = OrderCreationForm
    if request.method == 'POST':
        print(request.POST)
        form = OrderCreationForm(request.POST ,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            return HttpResponse("file cant upload") 
    context= {"form":form,"order":order}
    return render(request,"adminapp/order.html",context)



def order_update(request,pk):
    order = get_object_or_404(Orders,id=pk)
    form = OrderCreationForm(instance=order)
    if request.method == 'POST':
        print(request.POST)
        form = OrderCreationForm(request.POST, request.FILES,instance=order)
        if form.is_valid():
            form.save()
        return redirect('order')
    context = {'form':form}
    return render (request,"adminapp/order_update.html",context)


def order_delete(request,pk):
    print(pk)
    order = get_object_or_404(Orders,id=pk)
    # if request.method == "POST":
    order.delete()
    return redirect('order')



def product_as_per_customer(request,pk):
    
    orders = Orders.objects.filter(order_by=pk)
    print(orders)
    context ={"orders":orders}

    return render(request,"adminapp/customer_order.html",context)