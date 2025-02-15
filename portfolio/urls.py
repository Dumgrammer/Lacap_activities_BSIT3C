from tkinter.font import names

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]