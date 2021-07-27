from django.contrib import admin
from django.urls import path
from webapp import views
urlpatterns = [
    path("", views.register, name='register'),
    path("login", views.loginuser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("index",views.index,name='index'),
    path("uploadimg",views.uploadimg,name='uploadimg'),
    path("autosuggest",views.autosuggest,name='autosuggest'),



]
   