from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all

    context = {'all_pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=pizza).order_by('pizza_id')

    context = {'pizzas':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)
