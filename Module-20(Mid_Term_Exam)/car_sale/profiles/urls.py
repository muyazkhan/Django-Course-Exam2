from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>/', views.DetailPostView.as_view(), name='product_details'),
    path('buy/<int:id>/', views.buy, name='buy'),
    path('profile', views.profile.as_view(), name='profile'),
]
