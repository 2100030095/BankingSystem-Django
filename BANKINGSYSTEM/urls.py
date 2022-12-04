"""BANKINGSYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from SBI.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('registration', registration,name='registration'),
    path('login_user', login_user,name='login_user'),
    path('base', base,name='base'),
    path('withdraw', withdraw,name='withdraw'),
    path('deposite', deposite,name='deposite'),
    path('transaction', transaction,name='transaction'),
    path('profile', profile,name='profile'),
    path('change_pass', change_pass,name='change_pass'),
    path('logout', logout,name='logout'),
    path('admin_login', admin_login,name='admin_login'),
    path('admin_home', admin_home,name='admin_home'),
    path('change_passwordadmin', change_passwordadmin,name='change_passwordadmin'),
    path('loans', loans,name='loans'),
    path('cards', cards,name='cards'),
    path('apply_loan', apply_loan,name='apply_loan'),
    path('apply', apply,name='apply'),
    path('transfer', transfer,name='transfer'),
    path('captcha/',include('captcha.urls')),
    path('test', test, name='test'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),




]
