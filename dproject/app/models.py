# to create models the phone ones except str lines we can write in to create mdoels work ok 
from django.db import models

class food(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  about = models.CharField(max_length=300) 
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  updated = models.DateTimeField(auto_now=True)
  created= models.DateTimeField(auto_now_add=True)
  class Meta:
      ordering=['-updated','-created']
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

def __str__(self):
  return f"{self.about}"

def __str__(self):
  return f"{self.phone}"
  
def __str__(self):
  return f"{self.joined_date}"
    
'''here we add from phone to str lines for admin 
work we are doing okkkk for phone and all we willl have to add more models we will update it
like we do with the name remember 
2nd step now we will go in admin.py again'''

