from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup,name="singup"),
    path('login/', views.userlogin.as_view(),name="login"),
    path('logout/', views.user_logout, name='logout'),
]
