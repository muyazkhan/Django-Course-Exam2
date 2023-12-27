from django.shortcuts import render, redirect
from .import forms
from . import models
# Create your views here.


def task(request):
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = forms.TaskForm()
    return render(request, 'task.html', {'task': task_form})

def EditTask(request,id):
    post = models.Task.objects.get(pk=id)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST ,instance=post)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = forms.TaskForm(instance=post)
        return  render(request,'task.html',{'task': task_form})
    
def DeleteTask(request,id):
    post = models.Task.objects.get(pk=id)
    post.delete()
    return redirect('home')

