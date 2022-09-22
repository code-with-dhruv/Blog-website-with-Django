
from logging import PlaceHolder
from django import forms
from home.models import Post


class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields =('title','author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','PlaceHolder':'Title goes here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','PlaceHolder':'Write your content here'}),



        }