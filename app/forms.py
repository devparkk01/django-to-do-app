from .models import Item
from django import forms

class ItemForm(forms.ModelForm) :
    class Meta :
        model = Item 
        fields = ['title' , 'status' , 'priority']

 