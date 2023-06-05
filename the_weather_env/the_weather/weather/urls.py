from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  #the path for our index view
    path('<str:city>/delete', views.delete_view ),    
]