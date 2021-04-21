from django import forms
from .models import Blog


class ModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'heading', 'desc', 'date']
