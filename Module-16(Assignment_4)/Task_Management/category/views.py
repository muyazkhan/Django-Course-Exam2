from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def category_add(request):
    if request.method == "POST":
        add_category = forms.add_category(request.POST)
        if add_category.is_valid():
            add_category.save()
            return redirect('home')
    else:
        add_category = forms.add_category()
    return render(request, 'category.html', {'category': add_category})
