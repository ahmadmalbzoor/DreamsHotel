from django.db import models
from django.db.models.base import Model

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

class Room(models.Model):
    desc=models.TextField()
    img_url=models.CharField(max_length=255)
    room_name=models.CharField(max_length=255)
    price=models.IntegerField()
    booking_by=models.ManyToManyField(Customer,through="Reversation")
    check_in=models.DateField()
    check_out=models.DateField()
    is_booked=models.BooleanField()
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


