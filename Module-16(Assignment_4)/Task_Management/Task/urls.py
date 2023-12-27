from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.task ,name="task"),
    path('edit/<int:id>',views.EditTask, name='edit'),
    path('delete/<int:id>',views.DeleteTask, name='delete'),
   
]