from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, MenuItem, Ingredient, MenuItemIngredient

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MenuItemSerializer(ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'category', 'name', 'description', 'price', 'ingredients']

    def get_ingredients(self, obj):
        return list(obj.ingredients.values_list('name', flat=True))

class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemIngredientSerializer(ModelSerializer):
    class Meta:
        model = MenuItemIngredient
        fields = "__all__"
        depth = 2

