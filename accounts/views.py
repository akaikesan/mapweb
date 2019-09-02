from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import CustomUser
from django.contrib.auth import authenticate,login





def index(request):
    if request.method == 'POST':
        #this data has key "email", "password"
        data = json.loads(request.body)

        account = CustomUser.objects.get(email=data["email"])

        if(account == None):

            return HttpResponse('Unauthorized',status=401)

        if (account.check_password(data["password"])):
            #is this right????????????????
            login(request,account)
            return HttpResponse(status=200)
        else:
            return HttpResponse('Unauthorized', status=401)
