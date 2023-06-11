from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("accounts/login/", views.loginUser, name="login"),
    path("signup", views.signup, name="signUp"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logout_user, name="logout"),
    path("forgotPassword", views.forgot_password, name="forgotpassword")

]
    

