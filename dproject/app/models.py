# to create models the phone ones except str lines we can write in to create mdoels work ok 
from django.db import models

class food(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  about = models.CharField(max_length=300) 
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True, blank=True)
  updated = models.DateTimeField(auto_now_add=True)
  created= models.DateTimeField(auto_now=True)
  
  
  class Meta:
      ordering=['-updated','-created']
      def __str__(self):
         return f"{self.firstname} {self.lastname}"


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f"{self.title} by {self.author}"


class fiction(models.Model):
    options = (
        ('horror', 'horror'),
        ('romance', 'romance'),
        ('crime', 'crime'),
        ('Dark fantasy','Dark fantasy')
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    genre = models.TextField(max_length=300, choices = options)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at'] 



from django.db import models
class deals(models.Model):

   options = (
        ('horror', 'horror'),
        ('romance', 'romance'),
        ('crime', 'crime'),
        ('Dark fantasy','Dark fantasy'))
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   published_date = models.DateField(null=True, blank=True)
   discount = models.IntegerField(null=True, blank=True)
   original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   genre = models.TextField(max_length=300,choices=options)
   updated_at = models.DateTimeField(auto_now_add=True)
   created_at = models.DateTimeField(auto_now=True)
   
   
   class Meta:
        ordering = ['-updated_at', '-created_at']
        
        def __str__(self):
            return f"{self.title} by {self.author}"
'''here we add from phone to str lines for admin 
work we are doing okkkk for phone and all we willl have to add more models we will update it
like we do with the name remember 
2nd step now we will go in admin.py again'''

