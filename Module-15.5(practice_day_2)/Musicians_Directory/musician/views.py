from django.shortcuts import render, redirect
from .import forms
from musician.models import musicians
# Create your views here.


def addMusician(request):
    if request.method == 'POST':
        form = forms.add_musician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_musician')
    else:
        form = forms.add_musician
    return render(request, 'musician.html', {'form': form})


def editMusician(request, id):
    musician = musicians.objects.get(pk=id)
    form = forms.add_musician(instance=musician)
    if request.method == 'POST':
        form = forms.add_musician(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician.html', {'form': form})

