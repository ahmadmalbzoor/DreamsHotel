from django.db import models
from django.db.models.base import Model
from datetime import date, timedelta,datetime
from time import gmtime, strftime
import re


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
    #     
        return errors

class Hotel(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


class Room(models.Model):
    desc=models.TextField()

    room_name=models.CharField(max_length=255)
    price=models.IntegerField()
    booking_by=models.ManyToManyField(Customer,through="Reversation") 
    hotel=models.ForeignKey(Hotel,related_name="hotelrooms",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reversation(models.Model):
    customer=models.ForeignKey(Customer, related_name="reversation_customer", on_delete = models.CASCADE)
    room=models.ForeignKey(Room, related_name="reversation_room", on_delete = models.CASCADE)
    hotel=models.ForeignKey(Hotel, related_name="reversation_hotel", on_delete = models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    total_price=models.IntegerField()


class RoomAvalability(models.Model):
    room=models.ForeignKey(Room,related_name="Avalability",on_delete=models.CASCADE)
    reserved_date=models.DateField()
    is_booked=models.BooleanField(default=False)



def isAvailable(start_date,end_date,room_id):

    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta = end_date  - start_date       # as timedelta

    user_dates=[]

    for i in range(delta.days + 1):
        print("hiiiiiiiiiiiii")
        day = start_date + timedelta(days=i)
        user_dates.append(day)

    this_room=Room.objects.get(id=room_id)

    for date in user_dates: 

        if(RoomAvalability.objects.get(room=this_room,reserved_date=date).is_booked==True):
            return False

        
    return True
    
    


def create_booking(first_name,last_name,email,phone,room_id,start_date,end_date):
    if(isAvailable(start_date,end_date,room_id)==True):
        print("jjjjjjjjjjjjjj")
        new_customer=Customer.objects.create(first_name=first_name,last_name=last_name,phone=phone,email=email)
        this_room=Room.objects.get(id=room_id)
    
        
    
        this_hotel=Hotel.objects.get(id=1)
        new_reservation=Reversation.objects.create(customer=new_customer,room=this_room,hotel=this_hotel,check_in=start_date,check_out=end_date,total_price=0)
        updateStatus(start_date,end_date,room_id)

    





    

        return new_reservation

def display_room(room_id):  
    this_room=Room.objects.get(id=room_id)
    
    return this_room.room_name



def updateStatus(start_date,end_date,room_id):


    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)
    delta = end_date  - start_date       # as timedelta

    user_dates=[]

    for i in range(delta.days + 1):
        print("i have updated the status of rooooooooom")
        day = start_date + timedelta(days=i)
        user_dates.append(day)

    this_room=Room.objects.get(id=room_id)

    for date in user_dates: 

        x=RoomAvalability.objects.get(room=this_room,reserved_date=date)
        x.is_booked=True
        x.save()


    