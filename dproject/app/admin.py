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

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "about","phone","joined_date")
admin.site.register(food,MemberAdmin)

from .models import Book
class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "published_date","description","price")
  
admin.site.register(Book, MemberAdmin)

from .models import fiction
class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "published_date","genre","price")
  
admin.site.register(fiction, MemberAdmin)



from .models import deals
class MemberAdmin(admin.ModelAdmin):
  list_display = ("title", "author", "published_date","genre","original_price","discount")
  
admin.site.register(deals, MemberAdmin)
'''note that we can click on any name and change it's date and time whatever'''
