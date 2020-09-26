from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wishes', views.wishes),
    path('logout', views.logout),
    path('wishes/new', views.make_wish),
    path('add_wish', views.add_wish),
    path('edit/<int:id>', views.edit),
    path('edit_wish/<int:id>', views.edit_wish),
    path('grant/<int:id>', views.grant_wish),
    path('delete_wish/<int:id>', views.delete_wish),
]