from django.shortcuts import redirect, render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello world!")

# above code was for only to create views
# below code was for only to create views
from django.http import HttpResponse
from django.template import loader



def app(request):
  templates = loader.get_template('helloworld.html')
  return HttpResponse(templates.render())


# the code below is for views for data to diplay on admin for data display tempate 
from django.http import HttpResponse
from django.template import loader
from .models import food

def home(request):
  mymembers = food.objects.all().values()
  template = loader.get_template('datadisplay.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def aboutus(request):
  return render(request,'aboutus.html')

def helloworld(request):
  return render(request,'helloworld.html')

def room(request):
  return render(request,'room.html')


#now we are doing crud(one one way) 2nd step after making room_form html file
from .form import foodForm
def createRoom(request):
  form=foodForm
  context={'form': form}
  return render (request,'room_form.html',context)
#now we will go to url.py
#now for another way crud we will add form and context ko
#bi fill krege bs or hn import bi krege room form ko


#below code is for that final change means to save the form 
#redirect is imported at the top 
def createRoom(request):
  form=foodForm()
  if request.method=="POST":
    form=foodForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form }
  return render (request, 'room_form.html',context)