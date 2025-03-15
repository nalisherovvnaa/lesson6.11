from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.db.utils import IntegrityError



# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                form.add_error('username', 'Bu username allaqachon olingan!')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


# Register View
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f"Welcome, {user.username}! Your account has been created 🎉")
#             return redirect('home')
#         else:
#             messages.error(request, "Registration failed. Please correct the errors below!")
#     else:
#         form = CustomUserCreationForm()
    
#     return render(request, 'accounts/register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully! ✅")
            return redirect('profile')
        else:
            messages.error(request, "Error updating profile!")
    else:
        form = CustomUserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form})

# Custom Logout View
def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out 👋")
    return redirect('login')



# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.decorators import login_required
# from .forms import CustomUserCreationForm, CustomUserUpdateForm

# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = CustomUserUpdateForm(instance=request.user)
#     return render(request, 'accounts/profile.html', {'form': form})
