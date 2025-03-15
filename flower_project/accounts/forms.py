from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Ro'yxatdan o'tish uchun forma
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image', 'password1', 'password2']

# Profil yangilash uchun forma
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image']
