from django.shortcuts import render
from django import template
import datetime
# Create your views here.

# register = template.Library()

# @register.filter(name='center')
# def center(value, width):
#     return value.center(int(width))

def index(request):
    add1 = {'current_date': datetime.datetime.now()}
    add2 = ['sakib', 'hasan', 'khan']
   
    number = 10
    name = 'shkib al hasan'
    name1 = ''
    data = {
        'lst' : ['PYTHON',
                 'IS',
                 'BEST']
    }
    my_list = [
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35},
    ]
    return render(request, 'index.html', {'name': name})
    # return render(request, 'index.html',  {'my_list': my_list})
    # return render(request, 'index.html', data)
    # return render(request, 'index.html',add1)
