from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from controller.vehicle_controller import *
from controller.booking_controller import *
from controller.vendor_controller import *

from module.api import *

import requests, json, jwt, base64, datetime, time

from django.template import RequestContext
# Create your views here.


def dashboard(request):
    usrtype = request.session['usrtype']

    if usrtype == 1:
        print(usrtype)
    else:
        print("Im not an ADMIN")
        return HttpResponseRedirect('/vendor/login')


    template = 'admin-error/404.html'
    return render(request, template)

def approval(request):
    try:
        if request.session['usrtype'] == 1 and request.session["usrp_status"]:
            token = request.session['token']

            #vehicle
            key = vehicle_controller(token)
            data = vehicle_controller.v_deactlist(key)
            vehicle_data = json.loads(data)

            #vendor
            vendor = vendor_controller(token)
            ven_data = vendor_controller.inactive_list(vendor)
            vendor_data = json.loads(ven_data)



            context = {"vehicle_data": vehicle_data["data"], "vendor_data": vendor_data["data"] }
            template = 'adminside/vehicle.html'
            return render(request, template, context)
        else:
            return HttpResponseRedirect('/vendor/login/')
    except:
        return HttpResponseRedirect('/vendor/login/')
    




def activate(request, id, v_type):

    token = request.session['token']
    v_id = {"id": id}
    vid = json.dumps(v_id)

    if v_type == 'vehicle':
        key = vehicle_controller(vid,token)
        res = vehicle_controller.v_activate(key)
        data = json.loads(res)    
        if data['code'] == '200':
            return HttpResponseRedirect('/admin/approval')
    elif v_type == 'vendor':
        key = vendor_controller(vid,token)
        res = vendor_controller.activate(key)
        data = json.loads(res)    
        if data['code'] == '200':
            return HttpResponseRedirect('/admin/approval')

    return HttpResponseRedirect('/admin/approval')
    
