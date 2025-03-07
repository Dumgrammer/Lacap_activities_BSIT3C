from tkinter.font import names

from django.core.management.commands.runserver import naiveip_re
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:id>', views.get_user, name="get_user"),
    path('add/', views.add_user, name="add_user"),
    path('update/<str:id>', views.update_user, name="update_user"),
    path('delete/<str:id>', views.delete_user, name="delete_user")
]