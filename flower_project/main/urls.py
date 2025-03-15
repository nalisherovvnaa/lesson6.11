from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
     path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('flowers/', views.flower_list, name='flower-list'),  
    path('flower/add/', views.add_flower, name='add_flower'),  
]
