from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def admin_login(request):
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user:
            login(request, user)
            return render(request, 'dashboard.html')
        else:
            return render(request, 'admin_login.html')
        
    return render(request, 'admin_login.html')


def dashboard(request):
    return render(request, 'dashboard.html')