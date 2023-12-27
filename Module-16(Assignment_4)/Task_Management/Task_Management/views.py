from django.shortcuts import render
from Task.models import Task



def home(request):
    task = Task.objects.all()
    return render(request, 'home.html',{'tasks': task})

# views.py
