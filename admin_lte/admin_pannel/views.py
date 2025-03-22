from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.


class CustomLoginView(LoginView):
    redirect_authenticated_user = True  # Redirect logged-in users immediately
    def get_success_url(self):
        return self.get_redirect_url() or '/dashboard/'  # Default if 'next' is missing



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use get() to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:  # Corrected authentication check
            login(request, user)  # Log the user in
            
            
            return redirect('/admin/dashboard')  # Redirect to dashboard if 'next' is missing
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'}) 

    return render(request, 'admin_login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')