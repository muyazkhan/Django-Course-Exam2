from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from . import forms

class AlbumCreateView(CreateView):
    model = Album
    form_class = forms.add_album
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')  

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = forms.add_album
    template_name = 'album.html'
    success_url = reverse_lazy('home')  

class AlbumDeleteView(DeleteView):
    model = Album
    queryset = Album.objects.all()
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
