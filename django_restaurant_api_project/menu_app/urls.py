from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoryViewSet.as_view({'get':'list', 'post':'create', 'update':'update'})),
    path('category/<int:pk>', views.CategoryViewSet.as_view({'get':'retrieve', 'post':'create', 'update':'update', 'delete':'destroy'})),
    path('menu-items', views.MenuItemViewSet.as_view({'get':'list', 'post':'create', 'update':'update'})),
    path('menu-item/<int:pk>', views.MenuItemViewSet.as_view({'get':'retrieve', 'post':'create', 'update':'update', 'delete':'destroy'})),
    path('ingredients', views.IngredientViewSet.as_view({'get':'list', 'post':'create', 'update':'update'})),
    path('ingredient/<int:pk>', views.IngredientViewSet.as_view({'get':'retrieve', 'post':'create', 'update':'update', 'delete':'destroy'})),
    path('menu-item-ingredients', views.MenuItemIngredientViewSet.as_view({'get':'list', 'post':'create', 'update':'update'})),
    path('menu-item-ingredient/<int:pk>', views.MenuItemIngredientViewSet.as_view({'get':'retrieve', 'post':'create', 'update':'update', 'delete':'destroy'})),
    
    path('secret', views.secret)
]
