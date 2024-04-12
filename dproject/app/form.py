from django.forms import ModelForm
from .models import food

class foodForm(ModelForm):
    class Meta:
        model=food
        fields='__all__'

#this is second way of crud means build in forms