from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from controller.client_controller import *
from controller.vehicle_controller import *
from controller.vendor_controller import *
from module.api import *

import requests, json, jwt, base64, datetime, time

from django.template import RequestContext

import base64
from django.contrib.auth import authenticate,login


def home(request):
    template = 'home/homepage.html'
    lis = vehicle_controller.v_type(None)
    datas = json.loads(lis)
    if not request.user.is_authenticated:
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    username, password = base64.b64decode(auth[1]).decode('utf-8').split(':')
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    if user is not None and user.is_active:
                        # handle your view here
                        try:
                            if request.session["usrtype"] == 3:
                                    
                                token = request.session["token"]
                                uid = request.session["uid"]
                                usrtype = request.session["usrtype"]

                                data = vehicle_controller(token)
                                vehicle = json.loads(vehicle_controller.v_list(data))

                                data1 = client_controller(token,uid)
                                profile = json.loads(client_controller.client_profile(data1))

                                client_id = profile["data"][0]["client_id"]

                                context = {'status':usrtype, 'c_id':client_id, "vehicle":vehicle["data"], 'datas':datas["data"]}     
                                response = render(request, template, context)
                                return response

                        except Exception as e:
                        
                            print(" ")

                        status = 0
                        client_id = 0
                        context = {'c_id':client_id, 'status':status, 'datas':datas["data"]}    
                        response = render(request, template,context)

                        # >>>>>>>>>>>>>>>>>>>>>>>>>
                        return response
        # otherwise ask for authentification
        response = HttpResponse("")
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic realm="restricted area"'
        return response
    else:
        # handle your view here
        try:
            if request.session["usrtype"] == 3:
                    
                token = request.session["token"]
                uid = request.session["uid"]
                usrtype = request.session["usrtype"]

                data = vehicle_controller(token)
                vehicle = json.loads(vehicle_controller.v_list(data))

                data1 = client_controller(token,uid)
                profile = json.loads(client_controller.client_profile(data1))

                client_id = profile["data"][0]["client_id"]
                fullname = "{fname} {lname}".format(fname = profile["data"][0]["fname"], lname = profile["data"][0]["lname"])

                context = {'status':usrtype, 'c_id':client_id, "vehicle":vehicle["data"], 'datas':datas["data"], 'fullname':fullname}     
                response = render(request, template, context)
                return response

        except Exception as e:
        
            print(" ")

        status = 0
        client_id = 0
        context = {'c_id':client_id, 'status':status, 'datas':datas["data"]}    
        response = render(request, template,context)

        # >>>>>>>>>>>>>>>>>>>>>>>>>
        return response

def vendorRegistration(request):

    # try:
    #     if request.session["usrtype"] == 2 or request.session["usrtype"] == None:
    if request.user.is_authenticated:
            if request.POST:
                body           = {}
                contact_person = {}
                contact_no     = {}

                contact_person["Fname"], contact_person["Lname"] = request.POST["Fname"], request.POST["Lname"]
                body["ContactPerson"]   = [contact_person]
                body["Address"]         = request.POST["address"]
                
                contact_no["mobile"], contact_no["tel"] = request.POST["mobile"], request.POST["tel"]
                body["Contact"]         = [contact_no]
                body["Email"]           = request.POST["Email"]
                body["Payment-Type"]    = request.POST["Payment"]
                body["CompanyName"]     = request.POST["CompanyName"]
                body["pwd"]             = request.POST["pwd"]
                body["usrtype"]         = "2"
                body["role"]            = "2"

                register_form = json.dumps(body)
                print(register_form)
                register      = vendor_controller(register_form)
                request       = vendor_controller.addvendor(register)
                print(request)
                
                return HttpResponseRedirect('../vendor/login')

            # except Exception as e:
            else:
                
                print("FALSE")

                status = 0
                client_id = 0
                context = {'c_id':client_id, 'status':status}      

                template = "home/vendor_registration.html"
                return render(request, template, context)
    else:
        return redirect('/')
