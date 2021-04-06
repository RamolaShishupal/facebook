from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import OrderForm,CreateUserForm
from django.forms import inlineformset_factory
from .filters import *
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

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
def customer(request,pk_test):

    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    myfilter=OrderFilter(request.GET,queryset=orders)
    orders=myfilter.qs

    context={'customer':customer,'orders':orders,'order_count':order_count,'myfilter':myfilter}
    return render(request, 'accounts/customer.html',context)
def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=5)

    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        print('Printing POST:',request.POST)


        # form =OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return  redirect('/')

    context={'formset':formset}
    return render(request,'accounts/order_form.html',context)
def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        print('Printing POST:',request.POST)


        form =OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return  redirect('/')

    context={'form':form}
    return render(request,'accounts/order_form.html',context)
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')





    context={'item':order}

    return render(request,'accounts/delete.html',context)
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        # context={}
    return render(request,'accounts/login.html')
def register(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+user)
            return redirect('login')
    context = {'form': form}


    return render(request,'accounts/register.html',context)