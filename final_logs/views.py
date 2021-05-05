from django.shortcuts import render

# Create your views here.

from .models import Pizza, Topping
from django.contrib.auth.decorators import login_required


@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by("date_added")

    context = {"pizzas": pizzas}

    return render(request, "final_logs/pizzas.html", context)


@login_required
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by("-date_added")

    context = {"pizza": pizza, "toppings": toppings}

    return render(request, "final_logs/pizza.html", context)


def index(request):
    """The home page for Final Log. """
    return render(request, "final_logs/index.html")
