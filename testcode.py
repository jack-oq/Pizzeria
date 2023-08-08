import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")


import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.all()

#for pizza in pizzas:
    #print(pizza.id, pizza.pizza_name)

p = Pizza.objects.get(id=1)
print(p.pizza_name)

pizzas = Pizza.objects.filter(pizza_name=p)

for p in pizzas:
    print(p.id, p)
