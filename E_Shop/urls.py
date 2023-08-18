from django.urls import path
from E_Shop.views import *
urlpatterns = [
    path('data/',data),
    path('',index, name="index"),
    path('product/', products),
    path('product-get/<int:id>/', productget, name="productdetails"),
    path('product-filter/<int:id>/',productfilter),
    path('register/', register),
    path('login/', login, name="login"),
    path('logout/',logout,name="logout"),
    path('profile/', profile, name="profile1"),
    path('buynow/',buynow,name="buy"),
    path('ordertable/',ordertable,name="myorder"),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('successview/',ordersucess,name="orderSuccessView"),
]