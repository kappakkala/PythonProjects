from django.forms import ModelForm
from .models import Rooms, Post

class Postbuilding(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'