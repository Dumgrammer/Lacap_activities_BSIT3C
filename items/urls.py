from django.urls import path

from portfolio.urls import urlpatterns
from . import views

app_name = "items"

urlpatterns = [
    path('', views.index, name="get_all_items"),
    path('<str:id>', views.get_item, name="get_item"),
    path('?search=item', views.search_items, name="search_items"),
    path('add/', views.add_item, name="add_item"),
    path('update/<str:id>', views.update_item, name="update_item"),
    path('delete/<str:id>', views.delete_item, name="delete_item")
]