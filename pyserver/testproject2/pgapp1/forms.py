from django.forms import ModelForm, Form
from .models import Rooms, Post
from django import forms
class Postbuilding(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class BuildingForm(forms.Form):
   building = forms.CharField(required=False)
