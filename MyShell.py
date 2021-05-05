import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_log.settings")

import django

django.setup()

from final_logs.models import Pizza, Topping

pizzas = Pizza.objects.all()

for p in pizzas:
    print(f"Pizza ID: {t.id} Pizza: {t}")

p = Pizza.objects.get(id=1)
print(p.Text)
print(p.date_added)

toppings = t.topping_set.all()
for topping in toppings:
    print(topping)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user_id)