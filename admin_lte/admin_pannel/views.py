from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:  
            login(request, user)
            
            
            return redirect('/admin/dashboard/')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'}) 

    return render(request, 'admin_login.html')


@login_required(login_url='/admin/')
def dashboard(request):
    return render(request, 'dashboard.html')




# ✅ View to List Users
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# ✅ View to Add a User
@login_required
def user_add(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully!")
            return redirect('user_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/user_form.html', {'form': form})

# ✅ View to Edit a User
@login_required
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('user_list')
    
    return render(request, 'users/user_edit.html', {'user': user})

# ✅ View to Delete a User
@login_required
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('user_list')



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect("dashboard")  # Redirect to dashboard after signup
    else:
        form = CustomUserCreationForm()
    
    return render(request, "register.html", {"form": form})

@login_required(login_url='/admin/')
def doners(request):
    return render(request, 'simple.html')