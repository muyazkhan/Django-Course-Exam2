from django import forms
from . import models

class add_album(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'