from django.http import request
from django.shortcuts import render,redirect
# from . import models
# from .models import *
# from django.contrib import messages
# import bcrypt

def index(request):
    return render(request,"index.html")

def rooms(request):
    if request.method=="POST":
        return render(request,"rooms.html")     
    else:
        return redirect('/')   

def cards(request):
    return render(request,"checkout.html")

def voucher(request):
    return render(request,"voucher.html")        

