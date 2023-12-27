
from django.urls import path
from .import views
urlpatterns = [
    path('singup/', views.singup, name='singup'),
    path('login/', views.user_login, name='loginpage'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name="logoutpage"), 
    path('pass_change/', views.pass_change, name="passchange"), 
    path('pass_change2/', views.pass_change2, name="passchange2"), 
]
