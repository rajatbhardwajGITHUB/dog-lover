from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("login", views.loginUser, name="login"),
    path("signup", views.signup, name="signUp"),
    path("dashboard", views.dashboard, name="dashboard")

]
    

