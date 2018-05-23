from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context,loader

from controller.booking_controller import *
from controller.client_controller import *
from controller.vehicle_controller import *
from module.api import *

import requests, json, jwt, base64, datetime, time

from django.template import RequestContext
from django.contrib import messages
# Create Views Here

def clientBooking(request):
    if request.session["usrtype"] == 3 and request.session['token']:
        usrtype     = request.session["usrtype"]
        usrp_status = request.session['usrp_status']
        token       = request.session['token']
        uid         = request.session["uid"]

        data1 = client_controller(token,uid)
        profile = json.loads(client_controller.client_profile(data1))

        c_id = profile["data"][0]["client_id"]
        fullname = "{fname} {lname}".format(fname = profile["data"][0]["fname"], lname = profile["data"][0]["lname"])

        if c_id > 0:
            data      = booking_controller(token)
            actlist   = json.loads(booking_controller.b_activelist(data))
            data2 = client_controller(token,c_id)
            single = json.loads(client_controller.client_single(data2))
            
            if actlist["code"] and single["code"] == '200':
                msg = '200'
            else:
                msg = '203'

            context = { 
                "book_list":actlist["data"],
                "client":single["data"][0], 
                'status':usrtype,
                "c_id":c_id,
                "msg":msg,
                "fullname":fullname
                }
            template = "client/client_booking.html"
            response = render(request, template, context)
        else:
            response = HttpResponseRedirect('/vendor/login')
    else:
        response = HttpResponseRedirect('/vendor/login')

    return response

def booking(request,v_id):

    if request.session["usrtype"] == 3 and request.session["token"]:       
        usrtype = request.session["usrtype"]
        token   = request.session["token"]
        uid = request.session["uid"]

        data1 = client_controller(token,uid)
        profile = json.loads(client_controller.client_profile(data1))

        c_id = profile["data"][0]["client_id"]
        fullname = "{fname} {lname}".format(fname = profile["data"][0]["fname"], lname = profile["data"][0]["lname"])
        if request.POST:

            body = {}
            body["client_id"] = c_id
            startdate         = request.POST["start_date"]
            defuse_sd         = startdate.split('T')
            enddate           = request.POST["end_date"]
            defuse_ed         = enddate.split('T')
            data = {}
            data["vehicleID"]  = v_id
            data["start_date"] = "{d} {t}:00".format(d=defuse_sd[0], t=defuse_sd[1])
            data["end_date"]   = "{d} {t}:00".format(d=defuse_ed[0], t=defuse_ed[1])

            data["picking_time"] = "{d} {t}".format(d=defuse_sd[0], t=request.POST["picking_time"])
            data["price"]        = request.POST["price"]
            data["wDriver"]      = request.POST["wDriver"]
            body["data"]         = [data]
            loc = {}
            
            loc["pointA"] = [request.POST["a_lat"],request.POST["a_lon"]]
            loc["pointB"] = [request.POST["b_lat"],request.POST["b_lon"]]
            
            body["location"] = [loc]

            data = json.dumps(body)
    
            reqdata = booking_controller(data,token)
            req     = booking_controller.b_entry(reqdata)

            log = json.loads(req)

            if log['code'] == '200':
                print(log)        
                return HttpResponseRedirect('/client/clientBooking/')
            else:
                print("ERROR")
                print(log['code'])
                messages.info(request, 'That Date is Already Exist, Try To Change Your Date! Thank You')
                return HttpResponseRedirect('../{v_id}'.format(v_id=v_id))
                
        context = {'status':usrtype,"c_id":c_id,"fullname":fullname}
        template = "client/booking.html"
        response = render(request, template, context)
    else:
        response = HttpResponseRedirect('/vendor/login')

    return response



# ==== CLIENT VEHICLE LIST ====

def clientVehicleList(request):
    lis = vehicle_controller.v_type(None)
    datas = json.loads(lis)
    print(request.POST,"HOYYY")
    try:
        if request.session["usrtype"] == 3 and request.session["token"]:
            token = request.session["token"]
            uid = request.session["uid"]
            print(uid,"UID")
            usrtype = request.session["usrtype"]

            if request.method == 'POST':
                if request.POST["now"] == "now":
                    body = {}
                    body["vehicle_type"] = request.POST["v_type"]
                    body["picking_time"] = "{}:00".format(request.POST["p_time"])

                    data = json.dumps(body)
                    reqdata = vehicle_controller(data,token)
                    details = json.loads(vehicle_controller.v_asapsearch(reqdata))
                    
                else:
                    body1 = {}
                    body1["vehicle_type"] = request.POST["v_type_later"]

                    sdate = request.POST["s_date_later"]
                    defuse_sd         = sdate.split('T')

                    edate = request.POST["e_date_later"]
                    defuse_ed         = edate.split('T')

                    body1["start_date"] = "{d} {t}:00".format(d=defuse_sd[0], t=defuse_sd[1])
                    body1["end_date"] = "{d} {t}:00".format(d=defuse_ed[0], t=defuse_ed[1])
                    body1["picking_time"] = "{d} {t}:00".format(d=defuse_sd[0], t=request.POST["p_time_later"])

                    data = json.dumps(body1)
                    reqdata = vehicle_controller(data,token)
                    details = json.loads(vehicle_controller.v_search(reqdata))

                data1 = client_controller(token,uid)
                profile = json.loads(client_controller.client_profile(data1))

                client_id = profile["data"][0]["client_id"]
                fullname = "{fname} {lname}".format(fname = profile["data"][0]["fname"], lname = profile["data"][0]["lname"])
                
                geturl = vehicle_controller(id)
                url    = vehicle_controller.get_imageurl(geturl)

                if details["code"] == '200':
                                
                    for i in details["data"]:
                        for e in range(i["imgcount"]):
                            count = e
                            img   = "{plate}_{count}".format(plate=i["platenumber"],count=count)

                    context = {
                                'status'    :   usrtype, 
                                'c_id'      :   client_id, 
                                'search'    :   details["data"],
                                'msg'       :   details["code"],
                                'count'     :   count,
                                'url'       :   url,
                                'datas'     :   datas["data"],  # Vehicle category list
                                'fullname'  :   fullname
                            }
                else:
                    context = {
                                'status'    :   usrtype, 
                                'c_id'      :   client_id, 
                                'search'    :   details["data"],
                                'msg'       :   details["code"],
                                'datas'     :   datas["data"],  # Vehicle category list
                                'fullname'  :   fullname
                            }

                template = 'client/client-vehicleList.html'
                response = render(request,template, context)
            else:
                response = HttpResponseRedirect('/vendor/login')
        return response
    except:
        response = HttpResponseRedirect('/vendor/login')

    return response