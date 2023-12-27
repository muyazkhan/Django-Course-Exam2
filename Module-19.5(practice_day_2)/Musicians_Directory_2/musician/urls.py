from django.urls import path
from .import views 

urlpatterns = [
    path('add/', views.MusicianCreateView.as_view(), name='add_musician'),
    path('edit/<int:pk>/', views.MusicianUpdateView.as_view(), name='edit_musician'),
    
]
