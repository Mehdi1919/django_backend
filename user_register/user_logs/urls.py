from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('getusers/', views.getusers, name='getusers'),
    path('updateuser/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete, name='delete'),
]
