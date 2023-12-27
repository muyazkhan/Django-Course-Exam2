from django import forms
from . import models

class add_musician(forms.ModelForm):
    class Meta:
        model = models.musicians
        fields = '__all__'