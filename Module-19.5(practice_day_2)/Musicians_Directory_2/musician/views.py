from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import musicians
from .import forms

class MusicianCreateView(CreateView):
    model = musicians
    form_class = forms.add_musician
    template_name = 'musician.html'
    success_url = reverse_lazy('add_musician')  

class MusicianUpdateView(UpdateView):
    model = musicians
    form_class = forms.add_musician
    template_name = 'musician.html'
    success_url = reverse_lazy('home') 
