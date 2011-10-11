from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import *
from django.shortcuts import render_to_response
import datetime
from geniiApp.models import *

def index(request):
    return render_to_response("index.html")  
def test(request):
    return render_to_response("test.html")  
def registration(request):
    return render_to_response("Reg_form.html")  


def RegisterUser(request):
    email_req = str(request.GET['email'])
    country_req = str(request.GET['country'])
    username_req = str(request.GET['username'])
    password_req= str(request.GET['password'])
    u = UserInfo(email=email_req,country=country_req,username=username_req,password=password_req)
    u.save()
    return HttpResponse("Data saved sucessfully")

