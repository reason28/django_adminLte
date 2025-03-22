from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'admin_pannel'

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/doners', doners, name='doners'),
    path('logout/', LogoutView.as_view(), name='logout'),
]