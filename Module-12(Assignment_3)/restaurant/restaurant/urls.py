<<<<<<< HEAD

from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', include('meal.urls')),
    path('about_us/', include('about_us.urls')),
    path('', views.home , name='home'),
]


=======

from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meal/', include('meal.urls')),
    path('about_us/', include('about_us.urls')),
    path('', views.home , name='home'),
]


>>>>>>> 415bd444ebe07c2e4277975bb5caedf0436e5ec0
