from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Flower
from .forms import FlowerForm


def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'main/home.html', {'flowers': flowers})


def home(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlowerForm()
        
    flowers = Flower.objects.all()
    paginator = Paginator(flowers, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'page_obj': page_obj, 'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')



def home(request):
    flowers = Flower.objects.all()
    return render(request, 'home.html', {'page_obj': flowers})

def add_flower(request):
    if request.method == "POST":
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlowerForm()

    return render(request, 'flower_form.html', {'form': form})


# # Home
# def home(request):
#     query = request.GET.get('q', '')
#     flowers = Flower.objects.filter(name__icontains=query)
#     paginator = Paginator(flowers, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'main/home.html', {'page_obj': page_obj, 'query': query})

# def flower_list(request):
#     flowers = Flower.objects.all()
#     return render(request, 'main/flower_list.html', {'flowers': flowers})


# CRUD
@login_required
def create_flower(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlowerForm()
    return render(request, 'main/flower_form.html', {'form': form})

@login_required
def update_flower(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES, instance=flower)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FlowerForm(instance=flower)
    return render(request, 'main/flower_form.html', {'form': form})

@login_required
def delete_flower(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == 'POST':
        flower.delete()
        return redirect('home')
    return render(request, 'main/flower_confirm_delete.html', {'flower': flower})

# About and Contact
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
