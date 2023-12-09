from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle

from .models import Category, MenuItem, Ingredient, MenuItemIngredient
from .serializers import CategorySerializer, MenuItemSerializer, IngredientSerializer, MenuItemIngredientSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [AnonRateThrottle]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [AnonRateThrottle]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    throttle_classes = [AnonRateThrottle]

class MenuItemIngredientViewSet(viewsets.ModelViewSet):
    queryset = MenuItemIngredient.objects.all()
    serializer_class = MenuItemIngredientSerializer
    throttle_classes = [AnonRateThrottle]

@api_view()
@permission_classes([IsAuthenticated])
def secret(req):
    return Response("secret message", 200)