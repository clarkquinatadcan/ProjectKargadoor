from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url

from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import  include, url

# from django.core.urlresolvers import resolve
from django.urls import resolve
from . import views


app_name = 'vendor'

urlpatterns = [
    path('login/',                              views.login,            name='login'),
    
    path('logout/',                             views.logout,           name='logout'),
    path('dashboard/',                          views.dashboard,        name='dashboard'),
    path('transaction/',                        views.transaction,      name='transaction'),
    path('calendar/',                           views.calendar,         name='calendar'),
    path('map/',                                views.map,              name='map'),
    path('accounts/',                           views.accounts,         name='accounts'),
    path('settings/',                           views.settings,         name='settings'),

    path('preview/',                            views.vendorPreview,    name='preview'),
    path('profile/<int:ven_id>/',               views.vendorProfile,    name='profile'),
    path('update/<int:ven_id>/',                views.vendorUpdate,     name='update'),

    # Vehicle Type
    path('vehicle/',                            views.vehicle,          name='vehicle'),
    path('vehicle/add-vehicle/',    views.addVehicle,       name='addVehicle'),
    path('vehicle/preview/<int:v_id>/',          views.vehiclePreview,   name='vehiclePreview'),
    path('vehicle/deactivation/<int:v_id>/',     views.reqDeactivate,    name='vehicleDeactivation'),
    path('vehicle/update/<int:v_id>/',           views.updateVehicle,    name='vehicleUpdate'),

    path('404/',                                views.error,            name='404'),

    path('socialauths/<str:socialauthtoken>/',  views.socialauths,            name='socialauths'),

    path('transaction/detail/<int:b_id>/',      views.transactionDetail, name='transactionDetail'),
    path('transaction/detail/confirmation/<int:b_id>/',      views.transactionActivate, name='transactionConfirmation'),

    path('vehicle/search',      views.search_vehicles, name='search_vehicles'),
    
    
]
