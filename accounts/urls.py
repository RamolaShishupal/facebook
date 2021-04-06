from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.register, name='register'),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_test>',views.customer,name='customer'),
    path('create_order/<str:pk>',views.createOrder,name='create_order'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
    path('logout/',views.logoutuser,name='logout'),
]