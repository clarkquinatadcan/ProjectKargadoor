from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context,loader

from controller.vendor_controller import *
from controller.booking_controller import *
from controller.vehicle_controller import *
from controller.user_controller import *
from controller.client_controller import *
from module.api import *

from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout,
    )
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm

import requests, json, jwt, base64, datetime, time

from django.shortcuts import (
    render_to_response
)
from django.template import RequestContext

# Create your views here.
def error_404(request):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    exp       = request.session['exp']

    # logic for session expired/.
    if unix_time >= int(exp):
        response = render(request,'error/404.html')  
    else:
        # user details/.
        token = request.session['token']
        data  = jwt.decode(token,verify=False)
        for i in data["profile"]:
            pass
        fullname = ("{} {}".format(i['firstname'],i['lastname']))
        print(fullname)
        address  = 'Sitio Avocado Lahug Cebu City'
        # end >.

        response = render(request,'vendor/404.html',{'fullname':fullname,'address':address})            
    return response
 
def error_500(request):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    exp       = request.session['exp']   

    # logic for session expired/.
    if unix_time >= int(exp):
        print("Session Expired")
        response = render(request,'vendor/404.html')  
    else:
        print("Session Started")
        # user details/.
        token = request.session['token']
        data  = jwt.decode(token,verify=False)
        for i in data["profile"]:
            print(i)
        fullname = ("{} {}".format(i['firstname'],i['lastname']))
        print(fullname)
        address  = 'Sitio Avocado Lahug Cebu City'
        # end >.
        response = render(request,'vendor/404.html',{'fullname':fullname,'address':address})            
    return response

def socialauths(request, socialauthtoken):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    data = socialauthtoken
    print(data)
    decode  = jwt.decode(data,verify=False)
    print("decoded>>{}".format(decode))
    request.session['token'] = data
    request.session['uid']   = decode['uid']
    request.session['exp']   = decode['exp']
    response = redirect('/Kadmin/index/')
    # >.
    if request.session['uid'] == '':
        print("No UID")
    else:
        request.session['usrtype'] = decode["profile"][0]["usrtype"]
        usrtype = request.session['usrtype']


    exp = request.session['exp']
    uid = request.session['uid']

    # checking session if Expired /.
    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if  usrtype == 1:
            print("Session Started")
            print("USER STATUS is : {}".format(usrtype))
            response = redirect('/Kadmin/index/')
        elif usrtype == 2:
            print("Session Started")
            print("USER STATUS is : {}".format(usrtype))
            response = redirect('/vendor/dashboard/')
        elif usrtype == 3:
            print("Session Started")
            print("USER STATUS is : {}".format(usrtype))
            response = redirect('/../../')
        else:
            response = redirect('/vendor/login/') 
    return response

def login(request):
    if request.user.is_authenticated:
            print("Hello")
            # Set time now /. UNIX TIME
            n         = datetime.datetime.now()
            unix_time = int(time.mktime(n.timetuple()))
            # end >.
            request.session["searchVehicle"] = []

            print(unix_time)
            # If method POST >.
            if request.method == "POST":
                username = None
                pwd      = None
                response = render(request, 'vendor/login.html')    
                if request.POST['username'] != None and request.POST['pass'] != None:

                    json_data = {"uname": request.POST['username'], "pwd": request.POST['pass']}
                    print(json_data,"LOG")
                    # Initialize object >.
                    reqData = controller(json_data)
                    data    = controller.login(reqData)



                    decode  = jwt.decode(data,verify=False)
                    print(data,"DECODE")
                    print(decode,"DECODE")

                    # Saved session >.
                    request.session['token'] = data
                    request.session['uid']   = decode['uid']
                    request.session['exp']   = decode['exp']
                    # >.
                    if request.session['uid'] == '':
                        print("No UID")
                    else:
                        request.session['usrtype'] = decode["profile"][0]["usrtype"]
                        request.session['usrp_status'] = decode["profile"][0]['usrp_status']
                        usrtype = request.session['usrtype']
                        usrp_status = request.session['usrp_status']
                        print(usrtype)
                        print(usrp_status,"\n\n")

                    exp = request.session['exp']
                    uid = request.session['uid']

                    # checking session if Expired /.
                    if unix_time >= int(exp):
                        print("Session Expired")
                        response = redirect('/vendor/login/')  
                    else:
                        if  usrtype == 1:
                            print("Session Started")
                            print("USER STATUS is : {}".format(usrtype))
                            response = redirect('/admin/approval/')
                        elif usrtype == 2 and usrp_status == 1:
                            print("Session Started")
                            print("USER STATUS is : {}".format(usrtype))
                            response = redirect('/vendor/dashboard/')
                        elif usrtype == 3:
                            print("Session Started")
                            print("USER STATUS is : {}".format(usrtype))
                            response = redirect('/../../')
                        else:
                            response = redirect('/vendor/login/') 
            # Refresh same page >.
            else:
                request.session['exp']   = unix_time
                request.session['uid']   = 0
                request.session['token'] = None
                request.session['usrtype'] = None
                request.session['usrp_status'] = None

                exp = request.session['exp']
                uid = request.session['uid']
                if unix_time >= int(exp):
                    print("Session Expired")
                    response = render(request, 'vendor/login.html')
                else:
                    print("Session Started")
                    response = redirect('/vendor/dashboard/')
            return response
    else:
        response = redirect('/')
    return response



"""
Mode: validate user account
"""










def error(request):
    template = "vendor/404.html"
    return render(request, template)

# Session Destroy >.
def logout(request):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    token     = request.session['token']
    print(token)
    if token:
        del token
    else:
        pass
    del request.session['uid']
    del request.session['exp']
    del request.session['usrtype']
    del request.session['usrp_status']

    request.session['exp'] = unix_time
    request.session['uid'] = 0
    request.session['usrtype'] = ''

    return redirect('/')

def return_data(request):
    return HttpResponse(message)
    

def dashboard(request):
    # Set time now /. UNIX TIME
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    exp = request.session['exp']
    uid = request.session['uid']
    usrtype = request.session['usrtype']
    print("USER TYPE : {}".format(usrtype))

    # checking session if Expired /.
    if unix_time >= int(exp):
        print("Session Expired")

        response = redirect('/vendor/login/')
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            print("Session Started")

            # user profile /.
            token = request.session['token']

            print(token)
            data  = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address  = 'Sitio Avocado Lahug Cebu City'
            # end >.

            book_key         = booking_controller(token)
            booking_current  = json.loads(booking_controller.b_currentlist(book_key))
            booking_future   = json.loads(booking_controller.b_futurelist(book_key))

            current_booking = booking_current["data"]
            future_booking = booking_future["data"]

            msg_codeC = booking_current["code"]
            msg_codeF = booking_future["code"]


            c_booking = []
            f_booking = []

            if msg_codeC == '200':
                for bc in current_booking:
                    cid = bc['client_id']
                    vid = bc['vehicleID']
                    client_key     = client_controller(token,cid)
                    vehicle_key    = vehicle_controller(token,vid)

                    client_name    = json.loads(client_controller.client_single(client_key))
                    vehicle_type   = json.loads(vehicle_controller.v_single(vehicle_key))

                    if vehicle_type["code"] == '204':
                        clientName     = ""
                        v_type         = ""

                    else:
                        clientName     = client_name['data'][0]['lname'] + " " + client_name['data'][0]['fname']

                        v_type         = vehicle_type['data'][0]['vechicle_type']
                        


                        c_book = {
                            'client_name':clientName,
                            'start_date':bc["start_date"],
                            'end_date':bc["end_date"],
                            'v_id':bc["vehicleID"],
                            'b_id':bc["bookingID"],
                            'vehicle_type':v_type   
                        }

                        c_booking.append(c_book)

            if msg_codeF == '200':
                for bf in future_booking:
                    cid = bf['client_id']
                    vid = bf['vehicleID']

                    client_key     = client_controller(token,cid)
                    vehicle_key    = vehicle_controller(token,vid)

                    client_name    = json.loads(client_controller.client_single(client_key))
                    vehicle_type   = json.loads(vehicle_controller.v_single(vehicle_key))


                    if vehicle_type['code'] == '204' or client_name['code'] == '203':
                        clientName     = ""
                        v_type         = ""
                    else:
                        clientName     = client_name['data'][0]['lname'] + " " + client_name['data'][0]['fname']
                        v_type         = vehicle_type['data'][0]['vechicle_type']



                        f_book = {
                            'client_name':clientName,
                            'start_date':bf["start_date"],
                            'end_date':bf["end_date"],
                            'v_id':bf["vehicleID"],
                            'b_id':bf["bookingID"],
                            'vehicle_type':v_type
                            
                        }
                        
                        f_booking.append(f_book)

                context = {
                    'address':address,
                    'fullname':fullname,
                    'c_booked':c_booking,
                    'f_booked':f_booking,
                    'msg_codeC': msg_codeC,
                    'msg_codeF': msg_codeF,
                    'total_booking':len(f_booking)
                    }
            else:
                context = {
                    'address':address,
                    'fullname':fullname,
                    }
            template = "vendor/dashboard.html"
            response = render(request, template, context)

        else:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response
    

def transaction(request):
    # Set time now /. UNIX TIME
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    exp = request.session['exp']
    uid = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    # checking session if Expired /.
    if unix_time >= int(exp):
        print("expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            print("Session Started")        
            # user profile /.
            token = request.session['token']
            data  = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address  = 'Sitio Avocado Lahug Cebu City'
            # end >.

            template = "vendor/transaction.html"        
            response = render(request, template, {'address':address,'fullname':fullname})

        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response

def calendar(request):
    # Set time now /. UNIX TIME
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    exp = request.session['exp']
    uid = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    # checking session if Expired /.
    if unix_time >= int(exp):
        print("Session Expiredired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            print("Session Started")

            # user details/.
            token = request.session['token']
            data  = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address  = 'Sitio Avocado Lahug Cebu City'
            # end >.


            booking_key = booking_controller(token)
            booking_list = json.loads(booking_controller.b_activelist(booking_key))

            prin = json.dumps(booking_list["data"][0], indent=4)

            template = "vendor/calendar.html"        
            response = render(request, template, {'address':address,'fullname':fullname})
        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')


    return response

def map(request):
    # Set time now /. UNIX TIME
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    exp = request.session['exp']
    uid = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    # checking session if Expired /.
    if unix_time >= int(exp):
        print("Session Expiredired")
        response = redirect('/vendor/login/') 
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            print("Session Started")

            # user details/.
            token = request.session['token']
            data  = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address  = 'Sitio Avocado Lahug Cebu City'
            # end >.
            
            template = "vendor/map.html"
            response = render(request, template, {'address':address,'fullname':fullname})

        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response

def settings(request):
    # Set time now /. UNIX TIME
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    exp = request.session['exp']
    uid = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            # user details/.
            token = request.session['token']
            data = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address = 'Sitio Avocado Lahug Cebu City'
            # end >.

            template = "vendor/settings.html"
            response = render(request, template, {'address':address,'fullname':fullname})

        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response


def vendorPreview(request):
    # Set variables/.
    token       = request.session['token']
    uid         = request.session['uid']
    print("\n",uid,"\n")
    vendor_list = vendor_controller(token, uid)
    exp         = request.session['exp']
    single_list = json.loads(vendor_controller.single_list(vendor_list))
    msg         = single_list["code"] # Code message
    print(single_list)
    # Set time now/.
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    # checking session if Expired /.
    
    if msg == '200':

        # user profile /.
        data  = jwt.decode(token,verify=False)
        for i in data["profile"]:
            pass
        for x in single_list["data"]:
            pass

        fullname = ("{} {}".format(i['firstname'],i['lastname']))
        address  = 'Sitio Avocado Lahug Cebu City'
        # end >.
        list            = vendor_controller(token)
        data_list       = json.loads(vendor_controller.get_list(list))
        inactive_list   = json.loads(vendor_controller.inactive_list(list))
        # print(data_list)

        context  = {"active":data_list["data"], "inactive":inactive_list["data"]}
        template = "vendor/vendor_preview.html"
        response =  render(request, template, context)
        
    if msg == '204':
        print(msg)
        template = "error/404.html"       
        response = render(request, template)

    return response

def vendorProfile(request, ven_id):
    # Set variables/.
    token       = request.session['token']
    vendor_list = vendor_controller(token, ven_id)
    exp         = request.session['exp']
    single_list = json.loads(vendor_controller.single_list(vendor_list))
    msg         = single_list["code"] # Code message
    print(msg)
    # Set time now/.
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    # checking session if Expired /.
    if  unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')
    else:
        if msg == '200':

            # user profile /.
            token = request.session['token']
            data = jwt.decode(token,verify=False)
            for i in data["profile"]:
                pass
            for x in single_list["data"]:
                pass

            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            address = 'Sitio Avocado Lahug Cebu City'
            # end >.
            context = {
                'fullname': fullname,
                'address' : address,
                'data' : x,
                }
            template = "vendor/vendor_profile.html"
            response = render(request, template, context)
        if msg == '204':
            print(msg)
            template = "error/404.html"       
            response = render(request, template)

    return response
    
def vendorUpdate(request, ven_id):
    # Set variables/.
    token       = request.session['token']
    vendor_list = vendor_controller(token, ven_id)
    exp         = request.session['exp']
    single_list = json.loads(vendor_controller.single_list(vendor_list))
    msg         = single_list["code"] # Code message
    print(msg)
    # Set time now/.
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    # end >.

    # checking session if Expired /.
    if  unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')
    else:
        if msg == '200':
            list            = vendor_controller(token, ven_id)
            single_list     = json.loads(vendor_controller.single_list(list))
            inactive_list   = json.loads(vendor_controller.inactive_list(list))

            for i in inactive_list["data"]:
                w = i["ven_id"]
                if ven_id == w:
                    data = i
                    
            for a in single_list["data"]:
                data = a

            if request.GET:
                body           = {}
                contact_person = {}
                contact_no     = {}
                data_status    = {}
                status         = request.GET["status"]

                contact_person["Fname"], contact_person["Lname"] = request.GET["Fname"], request.GET["Lname"]
                body["ContactPerson"]   = [contact_person]
                body["Address"]         = request.GET["address"]
                
                contact_no["mobile"], contact_no["tel"] = request.GET["mobile"], request.GET["tel"]
                body["Contact"]         = [contact_no]
                body["Email"]           = request.GET["Email"]
                body["Payment-Type"]    = request.GET["Payment"]
                body["CompanyName"]     = request.GET["CompanyName"]


                update_form = json.dumps(body)
                reg         = vendor_controller(update_form,token,ven_id)
                register    = vendor_controller.updatevendor(reg)

                data_status["id"] = ven_id
                status_id         = json.dumps(data_status)
                send              = vendor_controller(status_id,token)

                if status == "1":
                    sendstats = vendor_controller.activate(send)
                    print("{ \n\t ",status_id,"\n\n\t Status ID: ",ven_id," Activate Successfully \n }")
                elif status == "0":
                    sendstats = vendor_controller.deactivate(send)
                    print("{ \n\t ",status_id,"\n\n\t Status ID: ",ven_id," Deactivate Successfully \n }")
                else:
                    print("{ \n\t ",status_id," \n\n\t Status ID: ",ven_id," is already Activated \n }")
                
                return HttpResponseRedirect('/vendor/preview/')
            
            context  = {"i":data}
            template = "vendor/vendor_update.html"
            return render(request, template, context)
            
        if msg == '204':

            print(msg)
            template = "error/404.html"       
            response = render(request, template)

    return response




# *****************************************************************************************
                                # VEHICLE
# *****************************************************************************************
def vehicle(request):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    exp       = request.session['exp']
    uid       = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")
    print(uid,"ID")

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            # user details/.
            token = request.session['token']
            data = jwt.decode(token,verify=False)
            cont = {}

            print(data)
            for i in data["profile"]:
                print(i)
                
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            print(fullname)
            address = 'Sitio Avocado Lahug Cebu City'

            key             = vehicle_controller(token)

            data_list       = json.loads(vehicle_controller.v_list(key))
            inactive_list   = json.loads(vehicle_controller.v_deactlist(key))

            # Context Base Dictionary 
            cont = {
                'address':address,
                'fullname':fullname,
                'ven_id':uid}

            if data_list["code"] == '200':
                print("DATA LIST ",data_list["code"])
                for i in data_list["data"]:
                    for e in range(i["imgcount"]):
                        
                        count_act = e
                        img   = "{plate}_{count}".format(plate=i["platenumber"],count=count_act)
                        print(img)
                cont["vehicle_list"] = data_list["data"]
                cont["count_act"] = count_act
                cont["msg_act"] = data_list["code"]
            else:
                print("DATA LIST ",data_list["code"])
                cont["msg_act"] = data_list["code"]
            
            if inactive_list["code"] == '200':
                print("INACTIVE LIST ",inactive_list["code"])
                for i in inactive_list["data"]:
                    for e in range(i["imgcount"]):
                        
                        count_inact = e
                        img   = "{plate}_{count}".format(plate=i["platenumber"],count=count_inact)

                cont["vehicle_deactlist"] = inactive_list["data"]
                cont["count_inact"] = count_inact
                cont["msg_deact"] = inactive_list["code"]

            else:
                print("INACTIVE LIST ",inactive_list["code"])
                cont["msg_deact"] = inactive_list["code"]
            
                    
            geturl = vehicle_controller(id)
            url    = vehicle_controller.get_imageurl(geturl)
            cont["endpoint"] = url
            print(url)
            lis = vehicle_controller.v_type(None)
            datas = json.loads(lis)
            cont["datas"] = datas["data"]

            # context dictionary
            context = cont
            # end >.
            print("Session Started")
            template = "vendor/vehicle.html"
            response = render(request, template, context)
        else:
            response = HttpResponseRedirect('/vendor/login/')
    
    return response


def addVehicle(request):

    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    token     = request.session['token']
    exp       = request.session['exp']
    uid       = request.session['uid']
    usrtype = request.session['usrtype']

    print("USER TYPE : {}".format(usrtype))

    # VENDOR ID
    ven_id = uid
    
    usrtype = request.session['usrtype']

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            data = jwt.decode(token,verify=False)   
            # print(data)
            for i in data["profile"]:
                # print(i)
                pass
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            # print(fullname)
            address = 'Sitio Avocado Lahug Cebu City'
            
            if request.POST:
                body = {}
                body["vendor_id"] = ven_id 
                data = {}
                image_file = []

                data["vechicle_type"] = request.POST["v_type"]
                data["qty"]           = request.POST["qty"]
                data["price"]         = request.POST["price"]
                data["description"]   = request.POST["des"]
                data["tankcapacity"]  = request.POST["tankcap"]
                data["platenumber"]   = request.POST["plate"]
                data["stockonhand"]   = request.POST["soh"]
                data["capacity"]      = request.POST["capacity"]
                data["unit"]          = request.POST["unit"]

                # print(request.POST.getlist('yea'),"FILESSSS")
                for i in request.POST.getlist('images'):
                    q   = "{count_image}".format(count_image=i)
                    img = {"img-codex":q}
                    image_file.append(img)

                data["images"]       = image_file 
                body["vehicle_data"] = [data]

                vehicle_form = json.dumps(body)

                reg      = vehicle_controller(vehicle_form,token)
                register = vehicle_controller.v_entry(reg)

                return HttpResponseRedirect('/vendor/vehicle/')
            
            lis = vehicle_controller.v_type(None)
            datas = json.loads(lis)
            
            context = { 'address':address,'fullname':fullname, 'datas':datas["data"]}
            template = "vendor/vehicle_add.html"
            print("Session Started")
            response = render(request, template, context)
        elif usrtype != 2:
            print("You are not a vendor User!!")

            response = redirect('/vendor/login/')

    return response

def updateVehicle(request, v_id):
    # Vehicle category list
    lis = vehicle_controller.v_type(None)
    datas = json.loads(lis)
    # end >.
    vehicle_id = v_id
    token      = request.session['token'] 
    n          = datetime.datetime.now()
    unix_time  = int(time.mktime(n.timetuple()))
    exp        = request.session['exp']
    uid        = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            data = jwt.decode(token,verify=False)   
            print(data)
            for i in data["profile"]:
                print(i)
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            print(fullname)
            address = 'Sitio Avocado Lahug Cebu City'

            list            = vehicle_controller(token)
            data_list       = json.loads(vehicle_controller.v_list(list))

            for i in data_list["data"]:
                print(i["vehicle_id"],"VEHICLE ID")
                print(i["vendor_id"],"VENDOR_ID \n")
                ve_id  = i["vehicle_id"]
                ven_id = i["vendor_id"]
                if vehicle_id == i["vehicle_id"]:
                    print(i["vehicle_id"])
                    print("TRUE")
                    single = i
                    print("\n",single,"\n\n")

            print(data_list["data"])

            if request.POST:
                body = {}
                body["vendor_id"] = v_id 
                data = {}

                data["vechicle_type"] = request.POST["v_type"]
                data["qty"]           = request.POST["qty"]
                data["price"]         = request.POST["price"]
                data["description"]   = request.POST["des"]
                data["stockonhand"]   = request.POST["soh"]
                data["capacity"]      = request.POST["capacity"]
                data["unit"]          = request.POST["unit"]
                
                body["vehicle_data"]  = [data]

                vehicle_form = json.dumps(body)
                print(vehicle_form," VEHICLE UPDATE")
                
                reg      = vehicle_controller(vehicle_form,token,v_id)
                register = vehicle_controller.v_update(reg)
                print(register)

                return HttpResponseRedirect('../../')

            context = { 'address':address,'fullname':fullname, 'i':single, "datas":datas["data"]}
            template = "vendor/vehicle_update.html"
            print("Session Started")
            response = render(request, template, context)
            
        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response

   

def vehiclePreview(request, v_id):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    token     = request.session['token']
    exp       = request.session['exp']
    uid       = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            data = jwt.decode(token,verify=False)   
            print(data)
            for i in data["profile"]:
                print(i)
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            print(fullname)
            address = 'Sitio Avocado Lahug Cebu City'

            context = { 'address':address,'fullname':fullname, 'v_id':v_id}
            template = "vendor/vehicle_preview.html"
            print("Session Started")
            response = render(request, template, context)
        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response


def reqDeactivate(request, v_id):
    token     = request.session['token']

    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    exp       = request.session['exp']
    uid       = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    if unix_time >= int(exp):
        print("Session Expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
            data_file = jwt.decode(token,verify=False)   
            print(data_file)
            for i in data_file["profile"]:
                print(i)
            fullname = ("{} {}".format(i['firstname'],i['lastname']))
            print(fullname)
            address = 'Sitio Avocado Lahug Cebu City'

            if request.POST:
                data                = {}
                data["id"]          = v_id
                data["particulars"] = request.POST["particulars"]
                
                if data["particulars"] == "":
                    print("None")
                else:
                    print("Valid")
                    data_req = json.dumps(data)
                    reg      = vehicle_controller(data_req,token,v_id)
                    register = vehicle_controller.v_reqdeactivate(reg)
                    print(register)
                
                return HttpResponseRedirect('../../')

            context = { 'address':address,'fullname':fullname}
            template = "vendor/vehicle_deactivation.html"
            print("Session Started")
            response = render(request, template, context)
        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response

def accounts(request):
    n         = datetime.datetime.now()
    unix_time = int(time.mktime(n.timetuple()))
    exp       = request.session['exp']
    uid       = request.session['uid']
    usrtype = request.session['usrtype']

    print(usrtype,"USERTYPE")

    if unix_time >= int(exp):
        print("expired")
        response = redirect('/vendor/login/')  
    else:
        if usrtype == 2 and request.session['usrp_status'] == 1:
                
            template = "vendor/calendar.html"
            print("Session Started")
            response = render(request, template)

        elif usrtype != 2:
            print("You are not a vendor User!")

            response = redirect('/vendor/login/')

    return response
        


def transactionDetail(request, b_id):
    token = request.session['token']
    print(b_id)
    book_key = booking_controller(token,b_id)


    booking_details  = json.loads(booking_controller.booking_single(book_key))

    # print(booking_details["data"])
    for data in booking_details["data"]:
        pass

    context = {
        'data':data
    }
    

    template = 'vendor/view_transaction.html'
    response = render(request,template, context)
    return response

def transactionActivate(request, b_id):
    token = request.session['token']

    book_key = controller(token,b_id)

    booking_activate  = json.loads(controller.booking_activate(book_key))

    return redirect('/vendor/transaction/detail/{}/'.format(b_id))
    
def search_vehicles(request):
    token = request.session['token']
    vehicle_key = vehicle_controller(token)

    vehicle_list = json.loads(vehicle_controller.v_list(vehicle_key))
    print("vehicle_list")

    for i in vehicle_list["data"]:
        for e in range(i["imgcount"]):
            count = e
            img   = "{plate}_{count}".format(plate=i["platenumber"],count=count)
            
    geturl = vehicle_controller(id)
    url    = vehicle_controller.get_imageurl(geturl)
    print(url)

    context = {
        "data":vehicle_list["data"],
        "count":count,
        "url":url
    }

    template = 'vendor/z_dummy_search.html'
    response = render(request,template, context)

    return response 