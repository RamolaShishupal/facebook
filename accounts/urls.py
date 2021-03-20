from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('product/',views.product,name='login'),
    path('customer/',views.customer,name='register'),
]