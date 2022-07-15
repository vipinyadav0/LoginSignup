from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('',views.home_page, name="home"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_page, name= 'signup'),
]
