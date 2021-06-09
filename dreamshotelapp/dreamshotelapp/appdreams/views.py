from django.http import request
from django.shortcuts import render,redirect
# from . import models
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request,"index.html")

def rooms(request):
    if request.method=="POST":
        request.session['check_in']=request.POST['check_in']
        request.session['check_out']=request.POST['check_out']
        request.session['adults']=request.POST['adults']

        return render(request,"rooms.html")     
    else:
        return redirect('/')   

# def rooms2(request):
#     errors = Customer.objects.login_validator(request.POST)
#         # check if the errors dictionary has) anything in it
#     if len(errors) > 0:
#         if request.method=="POST":
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#             for key, value in errors.items():
#                 messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#             return redirect('/')
#     else:
#         if request.method=="POST": 
#             check_in=request.POST["check_in"]
#             check_in=request.POST["check_out"]
#             adults=request.POST["adults"]
#             # new_reserv=models.create_booking(first_name,last_name,email,phone)
#             return redirect('/rooms')




# def cards2(request):
#     errors = Customer.objects.basic_validator(request.POST)
#         # check if the errors dictionary has) anything in it
#     if len(errors) > 0:
#         if request.method=="POST":
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#             for key, value in errors.items():
#                 messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#             return redirect('/cards')
#     else:
#         if request.method=="POST": 
#             print("llllllllllllllllllllll")
#             print(request.POST["first_name"])
#             first_name=request.POST["first_name"]
#             last_name=request.POST["last_name"]
#             email=request.POST["email"]
#             phone=request.POST['mobile']
#             # new_reserv=models.create_booking(first_name,last_name,email,phone)
#             return redirect('/voucher')        

def cards(request):
    return render(request,"checkout.html")    

# def cards2(request):
#     errors = Customer.objects.basic_validator(request.POST)
#         # check if the errors dictionary has) anything in it
#     if errors and len(errors) > 0:
#         if request.method=="POST":
#         # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
#             for key, value in errors.items():
#                 messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#             return redirect('/cards')
#     else:
#         if request.method=="POST": 
#             first_name=request.POST["first_name"]
#             last_name=request.POST["last_name"]
#             email=request.POST["email"]
#             phone=request.POST['mobile']
#             room_id=request.session['id']
#             start_date=request.session['check_in']
#             end_date=request.session['check_out']
#             new_reserv=models.create_booking(first_name,last_name,email,phone,room_id,start_date,end_date)
#             return redirect('/voucher')

def voucher(request):


    # errors = Customer.objects.basic_validator(request.POST)
    #     # check if the errors dictionary has) anything in it
    # if errors and len(errors) > 0:
    #     if request.method=="POST":
    #     # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
    #         for key, value in errors.items():
    #             messages.error(request, value)
    #     # redirect the user back to the form to fix the errors
    #         return redirect('/cards')
    # else:
        if request.method=="POST": 
            print("heeeeeeeeeeeeeeeeeeeeeeee")
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            phone=request.POST['mobile']
            room_id=request.session['room_id']
            start_date=request.session['check_in']
            end_date=request.session['check_out']
            new_reserv=create_booking(first_name,last_name,email,phone,room_id,start_date,end_date)
            context={"new_reserv":new_reserv} 
            return render(request,"voucher.html",context)  



        return redirect("/cards")      



def choose_room(request,id):
    del request.session['room_id']
    if 'room_id' not in request.session:
        request.session['room_id']=id
        print(request.session['room_id'])
    
    if isAvailable(request.session['check_in'],request.session['check_out'],request.session['room_id'])==False:
        messages.error(request,"sorry this room is not available in these dates")


    return redirect('/middle')



def view_allrooms(request):

   
        
    this_room=display_room(request.session['room_id'])

    print(this_room)
    
    if  isAvailable(request.session['check_in'],request.session['check_out'],request.session['room_id'])==False:
        showBookButton='yes'
    else:
        showBookButton='No'

    noofnights=NumberofNights(request,request.session['check_in'],request.session['check_out'])
    this_room1=Room.objects.get(id=request.session['room_id'])
    total_price=this_room1.price*noofnights
    context={"this_room":this_room,"showBookButton":showBookButton,"noofnights":noofnights,"total_price":total_price}

    



    return render(request,'rooms.html',context)



def NumberofNights(request,start_date,end_date):

    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta = end_date  - start_date       # as timedelta


    noofnights=delta.days 
    return noofnights

