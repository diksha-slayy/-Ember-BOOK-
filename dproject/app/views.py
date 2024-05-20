from django.shortcuts import get_object_or_404, redirect, render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello world!")

# above code was for only to create views
# below code was for only to create views
from django.http import HttpResponse
from django.template import loader


from app.models import deals
# def app(request,pk):
#   mymembers = get_object_or_404(food, id=pk)
#   deal= deals.objects.all()
#   context = {
#     'mymembers': mymembers,
#     'deal':deal,
#   }
#   return render(request , 'app/datadisplay.html', context)

# the code below is for views for data to diplay on admin for data display tempate 
from django.http import HttpResponse
from django.template import loader
from .models import food

def home(request):
  mymembers = food.objects.all()
  template = loader.get_template('datadisplay.html') 
  deal= deals.objects.all()
  context = {
    'mymembers': mymembers,
    'deal':deal,
  }
  return HttpResponse(template.render(context, request))


def aboutus(request):
  return render(request,'aboutus.html',{})

# def helloworld(request):
#   return render(request,'helloworld.html')

from app.models import fiction
def fictions(request):
    fictions = fiction.objects.all()
    context = {'fictions': fictions}
    return render(request, 'helloworld.html', context)

from .models import Book

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'new.html', context)




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



# al the above code is for food model means for form we do 


# now we are doing for Book model

from .form import BookForm
def AUTHOR(request):
  form=BookForm
  context={'Book':Book}
  return render (request,'room_form.html',context)


def AUTHOR(request):
  form=BookForm()
  if request.method=="POST":
    form=BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  context = {'form': form }
  return render (request, 'room_form.html',context)

from .form import fictionForm
def fict(request):
  form=fictionForm
  context={'fiction':fiction}
  return render (request,'room_form.html',context)


def fict(request):
  form=fictionForm()
  if request.method=="POST":
    form=fictionForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('fictions')
  context = {'form': form }
  return render (request, 'room_form.html',context)


#below code is for update means edit buttton
def updateRoom(request,pk):
  foods = food.objects.get(id=pk)
  form= foodForm(instance=foods)
  if request.method=='POST':
    form=foodForm(request.POST,instance=foods)
    if form.is_valid():
      form.save()
      return redirect(home)
  context={'form':form}
  return render(request, 'room_form.html',context)


def updatefictRoom(request,pk):
  fictions = fiction.objects.get(id=pk)
  form = fictionForm(instance=fictions)
  if request.method=='POST':
    form = fictionForm(request.POST,instance=fictions)
    if form.is_valid():
      form.save()
    return redirect('helloworld.html')
  context={'form':form}
  return render(request, 'room_form.html',context)

def updateAUTHORRoom(request,pk):
  books = Book.objects.get(id=pk)
  form = BookForm(instance=books)
  if request.method=='POST':
    form = BookForm(request.POST,instance=books)
    if form.is_valid():
      form.save()
      return redirect('new.html')
  context={'form':form}
  return render(request, 'room_form.html',context)



#BELOW CODE IS TO DELETE\

def deleteRoom(request,pk):
  foods=food.objects.get(id=pk)
  if request.method=='POST':
    foods.delete()
    return redirect('home')
  return render(request, 'delete.html' ,{'obj':foods})

def deletefictRoom(request,pk):
  fictions=fiction.objects.get(id=pk)
  if request.method=='POST':
    fictions.delete()
    return redirect('helloworld.html')
  return render(request, 'delete.html' ,{'obj':fictions})

def deleteAUTHORRoom(request,pk):
  books=Book.objects.get(id=pk)
  if request.method=='POST':
    books.delete()
    return redirect('new.html')
  return render(request, 'delete.html' ,{'obj':books})