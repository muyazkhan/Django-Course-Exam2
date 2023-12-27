from django import forms
from .models import Brand,Car,Comment


class car(forms.ModelForm):
  class Meta:
    model = Car
    fields ='__all__'


class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ['name', 'email', 'body']
        