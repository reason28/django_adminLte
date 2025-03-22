from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', include('admin_pannel.urls', namespace='admin_pannel')),
    path('login/', auth_views.LoginView.as_view(template_name='admin_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/admin/'), name='logout'),
    # path('another_app/', include('another_app.urls', namespace='another_app')),
    path('radmin/', admin.site.urls),
]
