from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]
# above code was for only to create views
# below code is for data one html we made 
urlpatterns = [
   # path('app/<str:pk>/', views.app, name='app'),
   path('', views.home, name='home'),# to open the home page dztadisplay wala template
   path('books/', views.book_list, name='book_list'),#for books means new arrivals ko kholne k lie
   path('deals_list/', views.home, name='datadispplay.html'),#for deals
   path('aboutus/', views.aboutus, name='aboutus.html'),#for about us contact ko kholne k lie 
   # path('helloworld/<str:pk>/', views.helloworld, name='helloworld.html'),#for helloworld ptani ku
   path('fictions/', views.fictions, name='fictions'),#for fictions means fiction books ko kholne k lie
   path('fictions/<str:pk>/', views.fictions, name='fictions'),
   path('aboutus/fictions', views.fictions, name='helloworld.html'),#from contact to fiction books
   path('books/helloworld/', views.fictions, name='helloworld.html'),#from new arriavls to fiction and also that link we have in new arribals
   path('books/fictions/', views.fictions, name='helloworld.html'),#from new arriavls to fiction
   path('aboutus/books', views.book_list, name='new.html'),#from contacts to new arriavls
   path('fictions/books', views.book_list, name='new.html'),#from fiction to new arrivals
   path('fictions/aboutus', views.aboutus, name='aboutus.html'),#from fiction to contact
   path('books/aboutus', views.aboutus, name='aboutus.html'),#from new arrivals to contact
   path('aboutus/aboutus', views.aboutus, name='aboutus.html'),#from loop chlane k lie
   path('fictions/fictions', views.fictions, name='helloworld.html'),#from loop chlane k lie
   path('books/books', views.book_list, name='new.html'),#from loop chlane k lie
   path('fictions/home', views.home, name='datadisplay.html'),#from fiction to home
   path('aboutus/home', views.home, name='datadisplay.html'),#from contacts to home
   path('books/home', views.home, name='datadisplay.html'),#from new arrivals to home
   path('create-room/',views.createRoom, name="create-room"),#one way crud
   path('AUTHOR/',views.AUTHOR, name="AUTHOR"),#one way crud
   path('fict/',views.fict, name="fict"),#one way crud
   path('fict/books',views.book_list, name="new.html"),#from fictional books crud to new arrivals 
   path('fict/aboutus',views.aboutus, name="aboutus.html"),#from fictional books crud to about us
   path('fict/fictions',views.fictions, name='helloworld.html'),#from fictional books crud to fiction to its own page
   path('AUTHOR/aboutus',views.aboutus, name="aboutus.html"),#from new arrivals crud to about us
   path('AUTHOR/fictions',views.fictions, name="helloworld.html"),#from new arrivals crud to fictions
   path('AUTHOR/books',views.book_list, name="new.html"),#from new arrivals crud to its own new arrival page
   path('create-room/fictions',views.fictions, name="helloworld.html"),#from home crud to fiction books
   path('create-room/books',views.book_list, name="new.html"),#from home crud to new arivals
   path('create-room/aboutus',views. aboutus, name=" aboutus.html"),#from home crud to aboutus
   path('create-room/home',views.home, name='datadisplay.html'),#from home crud to its own page
   path('update-room/<str:pk>/',views.updateRoom, name="update-room"),# update the fields of the datdisplay template
   path('updatefict-room/<str:pk>/',views.updatefictRoom, name="updatefict-room"),# update the fields of the fiction books means helloworld template
   path('updateAUTHOR-room/<str:pk>/',views.updateAUTHORRoom, name="updateAUTHOR-room"),# update the fields of the new arrival means helloworld template
   path('delete-room/<str:pk>/',views.deleteRoom, name="delete-room"),# delete the fields of the datdisplay template
   path('deletefict-room/<str:pk>/',views.deletefictRoom, name="deletefict-room"),# delete the fields of the fiction books helloworld template
   path('deleteAUTHOR-room/<str:pk>/',views.deleteAUTHORRoom, name="deleteAUTHOR-room"),# delete the fields of the NEW ARRIVALS template
]