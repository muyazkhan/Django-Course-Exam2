from django.shortcuts import render
# from . forms import contactForm
from .models import Testmodel
# Create your views here.


# def django_form(request):
#     if request.method == 'POST':
#         form = contactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = contactForm()
#     return render(request, 'home.html', {'form': form})

def home(request):
    students = Testmodel.objects.all()  # Note the use of parentheses ()
    return render(request, "home.html", {"students": students})
