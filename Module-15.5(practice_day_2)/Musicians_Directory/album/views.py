from django.shortcuts import render,redirect
from . import forms
from album.models import Album
# Create your views here.

def AddAlbum(request):
    if request.method == 'POST':
        form = forms.add_album(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAlbum')
    else:   
        form = forms.add_album() 
    return render(request,'album.html',{"form":form})

def editalbum(request, id):
    album = Album.objects.get(pk=id)
    form = forms.add_album(instance=album)
    if request.method == 'POST':
        form = forms.add_album(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'album.html', {'form': form})



def deletealbum(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')