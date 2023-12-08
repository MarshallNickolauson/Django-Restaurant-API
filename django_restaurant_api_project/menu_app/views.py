from rest_framework import viewsets

from .models import Category, MenuItem, Ingredient, MenuItemIngredient
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer, MenuItemIngredientSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class MenuItemIngredientViewSet(viewsets.ModelViewSet):
    queryset = MenuItemIngredient.objects.all()
    serializer_class = MenuItemIngredientSerializer