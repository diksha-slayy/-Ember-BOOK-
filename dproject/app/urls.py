from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]
# above code was for only to create views
# below code is for data one html we made 
urlpatterns = [
   path('app/', views.app, name='app'),
   path('', views.home, name='home'),
   path('helloworld/', views.helloworld, name='helloworld.html'),
   path('room/', views.room, name='room.html'),
   path('aboutus/', views.aboutus, name='aboutus.html'),
   path('create-room/',views.createRoom, name="create-room"),#one way crud
]