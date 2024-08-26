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
    path("edit_myexperience", views.edit_myexperience, name="edit_myexperience"),
    path("my_education", views.my_education, name="my_education"),
    path("edit_myeducation", views.edit_myeducation, name="edit_myeducation"),

]
