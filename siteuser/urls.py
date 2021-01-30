from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register,name='register-user'),
    path('login', views.login,name='login-user'),
    path('logout', views.logout,name='logout-user'),
    path('profile', views.profile,name='profile-user')

]
