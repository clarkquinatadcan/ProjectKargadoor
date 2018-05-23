from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url

from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import  include, url

# from django.core.urlresolvers import resolve
from django.urls import resolve
from . import views


app_name = 'home'

urlpatterns = [
    path('',    		views.home,     				name='homepage'),
    path('register/', 	views.vendorRegistration,		name='vendorRegistration'),

]