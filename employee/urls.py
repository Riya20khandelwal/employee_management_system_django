from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path("emp_login", views.emp_login, name="emp_login"),
    
]
