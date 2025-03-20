from django.urls import path
from .views import *

app_name = 'admin_pannel'

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
]