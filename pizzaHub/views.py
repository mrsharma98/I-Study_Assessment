from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzaHub/home.html', {'pizzas':pizzas})

@login_required
def detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, "pizzaHub/detail.html", {'pizza':pizza})
