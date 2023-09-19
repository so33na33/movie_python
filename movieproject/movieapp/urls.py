from django.contrib import admin
from django.urls import path, include
from . import views

app_name='movieapp'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('movie/<int:movie_id>/',views.detail,name="detail"),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
