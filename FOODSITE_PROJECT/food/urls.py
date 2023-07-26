from django.urls import path
from . import views


app_name= 'food'

urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('process/', views.process,name='process'),
    path('', views.item,name="item"),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add/', views.add_item,name="add_item"),
    path('update/<int:id>/', views.update_item,name="update_item"),
    path('delete/<int:id>/', views.delete_item,name="delete_item"),
    
    
]
