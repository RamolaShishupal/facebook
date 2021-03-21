from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_test>',views.customer,name='customer'),
]