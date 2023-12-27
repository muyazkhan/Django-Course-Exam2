from django.urls import path
from . import views
urlpatterns = [
    path('', views.addMusician,name="add_musician"), 
    path('edit/<int:id>', views.editMusician, name='editMusician'),
]
