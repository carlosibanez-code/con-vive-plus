from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, houses_list,my_account, logout_user, register_user

urlpatterns = [
    path("", home, name= 'home'),
    path("houses/", houses_list, name = 'houses'),
    path("login/", auth_views.LoginView.as_view(template_name = 'con_vive_plus/login.html'), name = 'login'),
    path("logout/", logout_user, name = 'logout'),
    path("register/", register_user, name = 'register'),
    path("my-account/", my_account, name = 'my_account'),
]