from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def index(request):
    if request.method == 'POST':
        b = request.body
        data = json.loads(b)

        mEmail = data["email"]
        mPassword = data["password"]

        account = User.objects.get(email=mEmail)

        if(account == None):

            return HttpResponse('Unauthorized',status=401)

        authed = account.check_password(mPassword)

        if (authed == True):
            return HttpResponse(status=200)
        else:
            return HttpResponse('Unauthorized', status=401)
