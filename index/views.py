from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def store(request):
    products=Product.objects.all()
    return render(request,"store.html",{'products':products})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
    return render(request,"cart.html", {'items':items, 'order':order})


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
    return render(request,"checkout.html",{'items': items,'order':order})




