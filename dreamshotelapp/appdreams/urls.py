from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path("cards",views.cards),
    path('voucher',views.voucher)
]