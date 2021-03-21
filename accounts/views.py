from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import  HttpResponse
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()


    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,'total_orders':total_orders,'total_customers':total_customers
               ,'delivered':delivered,'pending':pending}


    return render(request,'accounts/dashboard.html',context)
def product(request):
    products=Product.objects.all()
    return render(request, 'accounts/product.html',{'products':products})
def customer(request):
    return render(request, 'accounts/customer.html')