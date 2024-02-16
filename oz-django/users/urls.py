from django.urls import path
from . import views

urlpatterns =[
    path('', views.Users.as_view()),
    path('myinfo/', views.MyInfo.as_view()),
]