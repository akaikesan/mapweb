from django.shortcuts import render

# Create your views here.
import json
import datetime
import urllib.request
import boto3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tempfile
import base64
import io



from PIL import Image
from django.core.files import File
from django.conf import settings
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


import urllib.request

def comment(request):

    if request.method == 'POST':

        data = json.loads(request.body)
        Content.objects.create(accounts = request.user, content = data["content"],latitude = data["latitude"],longitude = data["longitude"])
        return HttpResponse()#its confirmed the fact that the AnonimousUser is set to request.user without session.


'''ValueError: unknown url type:
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


            jsondict["comment" + str(i)] = {
                "content":content.content,
                "fav":content.fav
            }

            i += 1

            if i > 20:
                break

        resp = HttpResponse()

        resp.content = json.dumps(jsondict,ensure_ascii=False)
        return resp

def pincomment(request):
    if request.method == 'POST':


        data = json.loads(request.body)


        lat = float(data['latitude'])

        lon = float(data['longitude'])

        lon_rng = float(data['lon_range'])

        lat_rng = float(2933.0/111263.0/2.0)

        contents = Content.objects.filter(longitude__range=[lon-lon_rng,lon+lon_rng],latitude__range=[lat - lat_rng,lat+lat_rng]).order_by('-date')[:23]
        i = 0
        jsondict = {}
        for content in contents:


            jsondict["comment" + str(i)] = {
                "username":content.accounts.username,
                "content":content.content,
                "fav":content.fav,
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




def imageResponse(request):
    if request.method == 'GET':
        """
        #your_media_root = settings.MEDIA_ROOT

        #url = get_public_url("mapsec","minimalism-1560688617481-8660.jpg")
        local_filename, headers = urllib.request.urlretrieve("https://mapsec.s3-ap-northeast-1.amazonaws.com/minimalism-1560688617481-8660.jpg")
        image_file = open(local_filename)
        s3 = boto3.resource('s3')

        bucket = s3.Bucket('mapsec')
        image_file=bucket.download_file('minimalism-1560688617481-8660.jpg', 'minimalism-1560688617481-8660.jpg')
        """
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('mapsec')
        obj = bucket.Object('minimalism-1560688617481-8660.jpg').get()
        tmp = tempfile.NamedTemporaryFile()


        stream = io.BytesIO(obj['Body'].read())

        img = Image.open(stream)


        img.show()

        print(img)

        if not img:
            return HttpResponse(status=200)

        return HttpResponse(File(stream), content_type="image/jpeg")
            #image_file = request.user.image


"""
def get_public_url(bucket, target_object_path):
    ------------------------------------------------------------------------------
    対象のS3ファイルのURLを取得する

    Parameters
    ----------
    bucket: string
        S3のバケット名
    target_object_path: string
        取得したいS3内のファイルパス

    Returns
    ----------
    url: string
        S3上のオブジェクトのURL
    ------------------------------------------------------------------------------
    bucket_location = s3.get_bucket_location(Bucket=bucket)
    return "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        bucket,
        target_object_path)
"""
