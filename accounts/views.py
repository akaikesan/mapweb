from django.shortcuts import render

# Create your views here.
import json
import datetime
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import CustomUser,Content
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.sessions.models import Session




def login(request):
    if request.method == 'POST':
        #this data has key "email", "password"
        data = json.loads(request.body)

        account = CustomUser.objects.get(email=data["email"])

        if(account == None):

            return HttpResponse('Unauthorized',status=401)

        if (account.check_password(data["password"])):

            auth_login(request,account)
            # セッションスタート
            if not request.session.session_key:
                request.session.create()

            mResponse = HttpResponse(status=200)

            #is this right????????????????
            return mResponse
        else:
            return HttpResponse('Unauthorized', status=401)



def comment(request):

    if request.method == 'POST':

        data = json.loads(request.body)
        Content.objects.create(accounts = request.user, content = data["content"],latitude = data["latitude"],longitude = data["longitude"])
        return HttpResponse()#its confirmed the fact that the AnonimousUser is set to request.user without session.


'''
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print("you use cookie")
        return HttpResponse("you use cookie")
    else:
        print("you dont use cookie")
        return HttpResponse("you dont use cookie")

    request.session.set_test_cookie()
'''


def profile(request):
    if request.method == 'GET':
        account = request.user

        contents = Content.objects.filter(accounts=request.user).order_by('-date')[:23]

        jsondict = {
            "introduce":account.self_introduce,
            "username":account.username,
        }

        i = 0

        for content in contents:


            jsondict["comment" + str(i)] = content.content

            i += 1

            if i > 20:
                break

        resp = HttpResponse()

        resp.content = json.dumps(jsondict,ensure_ascii=False)

        return resp

def pincomment(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        print(data)

        lat = float(data['latitude'])

        lon = float(data['longitude'])

        lon_rng = float(data['lon_range'])

        lat_rng = float(2933.0/111263.0/2.0)

        contents = Content.objects.filter(longitude__range=[lon-lon_rng,lon+lon_rng],latitude__range=[lat - lat_rng,lat+lat_rng]).order_by('-date')[:23]
        i = 0
        jsondict = {}
        for content in contents:


            jsondict["comment" + str(i)] = {
                "content":content.content,
                "latitude":content.latitude,
                "longitude":content.longitude
            }



            i += 1

            if i > 20:
                break

        resp = HttpResponse()

        resp.content = json.dumps(jsondict,ensure_ascii=False,default = decimal_default_proc)

        return resp


def decimal_default_proc(obj):
    from decimal import Decimal
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
