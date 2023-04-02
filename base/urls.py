from django.urls import path;
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('product/<str>', views.getProduct, name='product'),
]