from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'admin_pannel'

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]