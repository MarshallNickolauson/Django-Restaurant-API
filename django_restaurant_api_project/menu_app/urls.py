from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoryViewSet.as_view({'get':'list'})),
    path('category/<int:pk>', views.CategoryViewSet.as_view({'get':'retrieve'})),
]
