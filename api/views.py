from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from controller.controller import *
from controller.booking_controller import *
from controller.vehicle_controller import *
from module.api import *



import requests, json, jwt, base64, datetime, time


def booking_list(request):
    token = request.session['token']
    booking_key = booking_controller(token)
    booking_list = json.loads(booking_controller.b_activelist(booking_key))

    exam = booking_list["data"]


    b_list = []

    for i in booking_list["data"]:
        s_date = i['start_date']
        e_date = i['end_date']

        time_format="%a, %d %b %Y %H:%M:%S GMT"

        start = datetime.datetime.strptime(s_date, time_format)
        end = datetime.datetime.strptime(e_date, time_format)
        color = "#0{}".format(i["bookingID"])
        l_book = {
            'id':i["bookingID"],
            'title':i["booking_code"],
            'start':str(start),
            'end':str(end),
            'color':color
            }
        b_list.append(l_book)
        
    books = json.dumps(b_list, indent=4)
    return HttpResponse(books)

def vehicle_list(request):
    token = request.session['token']
    print(token)
    vehicle_key = vehicle_controller(token)

    vehicle_list = json.loads(vehicle_controller.v_list(vehicle_key))

    v_list = vehicle_list["data"]

    vl = json.dumps(v_list, indent=4)

    return HttpResponse(vl)

