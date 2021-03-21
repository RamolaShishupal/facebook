from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import  HttpResponse
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()

    context={'order':orders,'customers':customers}


    return render(request,'accounts/dashboard.html')
def product(request):
    products=Product.objects.all()
    return render(request, 'accounts/product.html',{'products':products})
def customer(request):
    return render(request, 'accounts/customer.html')