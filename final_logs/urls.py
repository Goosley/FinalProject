from django.urls import path

from . import views

app_name = "final_logs"

urlpatterns = [
    path("", views.index, name="index"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
]
