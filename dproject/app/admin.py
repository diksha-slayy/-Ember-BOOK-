# from django.contrib import admin

# Register your models here.
# from .models import food
# admin.site.register(food)
''' above here we are writing the code to show the templates on admin site after ceating the admin superuser
then we willl go to models.py and make models'''

'''now in below code again we are creating a class here for admin site for models heheh my english ahahah
'''
'''here we are giving another name to this class we can;t give the same name as we gave
in models so yeah also in this step wew ill comment the
admin on line 5 '''
from django.contrib import admin
from .models import food
class fictAdmin(admin.ModelAdmin):
  list_display=("firstname","lastname","joined_date","phone","about")
  
admin.site.register(food,fictAdmin)

'''note that we can click on any name and change it's date and time whatever'''
