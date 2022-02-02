from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from auth2 import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('', views.RegisterAPIView.as_view()),

]


