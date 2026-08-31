from django.contrib import admin

from .models import Pizza, Topping, Size, PizzaSize


admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Size)
admin.site.register(PizzaSize)