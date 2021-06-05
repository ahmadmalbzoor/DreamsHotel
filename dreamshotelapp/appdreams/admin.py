from django.contrib import admin
from django.contrib.admin import options
from django.contrib.admin.filters import ListFilter
from django.db.models.query_utils import FilteredRelation
from django.utils.html import format_html


from . import models
from .models import *

class RoomAdmin(admin.ModelAdmin):
     list_display = ('desc', 'room_name' , 'price' ,'hotel')


class HotelAdmin(admin.ModelAdmin):
      list_display = ('name', 'desc')

admin.site.register(Hotel , HotelAdmin)
admin.site.register(Room , RoomAdmin)