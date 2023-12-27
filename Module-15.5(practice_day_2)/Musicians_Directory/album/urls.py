from django.urls import path
from . import views
urlpatterns = [
    path('', views.AddAlbum,name="add_album"), 
    path('edit/<int:id>', views.editalbum, name='editalbum'),
    path('delete/<int:id>', views.deletealbum, name='deletealbum'),
]

