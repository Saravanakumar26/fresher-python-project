from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.login,name='login'),
    path('view/', views.register_read,name='register_read'),
    path('create/',views.register_create,name='create'),
    path('update/<pk>',views.register_update,name='update'),
    path('delete/<pk>',views.register_delete,name='delete'),
]
