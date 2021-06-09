from django.urls import path
from django.urls.conf import include     
from . import views
urlpatterns = [
    path('', views.index),
    path('rooms', views.rooms),
    path("cards",views.cards),
    path('voucher',views.voucher),
    #path('check',views.cards2),
    path('rooms/<int:id>',views.choose_room),
    path('middle',views.view_allrooms),
    # path('check',views.cards2),
    # path('rooms2',views.rooms2),
    ]
