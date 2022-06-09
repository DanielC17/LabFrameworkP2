
from django.urls import path
from produto import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
]
