from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path("emp_login", views.emp_login, name="emp_login"),
    path("emp_home", views.emp_home, name="emp_home"),
    path("profile", views.profile, name="profile"),
    path("logout", views.Logout, name="logout"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("my_experience", views.my_experience, name="my_experience"),
    path("edit_experience", views.edit_experience, name="edit_experience"),

]
