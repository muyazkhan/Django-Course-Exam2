
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import home
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include('authorization.urls')),
    path('', views.home,name="home"),
    path("brands/<slug:brand>", home, name="brand_name"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)