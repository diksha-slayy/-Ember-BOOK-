from django.forms import ModelForm
from .models import food
# for home page edit and add your books form
class foodForm(ModelForm):
    class Meta:
        model=food
        fields='__all__'

# for new arrivals edit and add your books form
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

# for fiction books edit and add your books form
from .models import fiction

class fictionForm(ModelForm):
    class Meta:
        model=fiction
        fields='__all__'

#this is second way of crud means build in forms