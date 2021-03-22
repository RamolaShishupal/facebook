from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_test>',views.customer,name='customer'),
    path('create_order/',views.createOrder,name='create_order'),
    path('update_order/',views.updateOrder,name='update_order'),
]