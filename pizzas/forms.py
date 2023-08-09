from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}
        