"""ispider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.booking),
    path('savesign/', views.saveSign, name="savesign"),
    path('savelogin/', views.saveLogin, name="savelogin"),
    path('savebook/', views.saveBook, name="savebook"),
    path('save_Contact/', views.saveContact, name="save_Contact"),

    path('home/',views.home),
    path('signup/',views.signup, name= "signup"),
    path('login/',views.login, name = "login"),
    path('booking/',views.booking, name = "booking"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name = "about"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('email_password/', views.email_password, name="email_password"),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('currentbooking/',views.currentbooking,name='currentbooking'),
    path('previousbooking/',views.previousbooking,name='previousbooking'),
    path('logout/',views.logout, name = "logout"),
    path('booknow/',views.booknow, name = "booknow"),
    path('cancel/<str:variable>', views.cancel, name='cancel'),
    
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
    path('reset/<uidb64>/<token>', views.reset, name="reset"),
    path('reset_pass/<uidb64>/<token>', views.reset_pass, name="reset_pass"),
    path('getdata/', views.getdata, name="getdata"),

    path('adminbook/', views.adminbook, name="adminbook"),
    path('adminbook2/', views.adminbook2, name="adminbook2"),
    path('bookbydate/', views.bookbydate, name="bookbydate"),

]
