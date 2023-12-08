from django.contrib import admin

from .models import Category, MenuItem, Ingredient, MenuItemIngredient

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(MenuItemIngredient)