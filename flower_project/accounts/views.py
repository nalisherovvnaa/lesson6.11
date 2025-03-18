from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.utils import IntegrityError
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import Post


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


def register(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        try:
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created 🎉")
            return redirect('home')
        except IntegrityError:
            form.add_error('username', 'This username is already taken!')
            messages.error(request, 'This username is already taken!')
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    form = CustomUserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Profile updated successfully! ✅")
        return redirect('profile')
    
    return render(request, 'accounts/profile.html', {'form': form})


def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You've been successfully logged out. See you soon! 👋")
    else:
        messages.warning(request, "You're not logged in!")
    return redirect('login')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = '/posts/'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = '/posts/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/posts/'
