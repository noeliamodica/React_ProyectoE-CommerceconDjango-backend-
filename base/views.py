from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products

# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/products/',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>',
        ]


    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    
    product = None
    for i in products:
        if i["id"] == pk:
            product = i
            break
    
    if product is not None:
        return Response(product)
    else:
        return Response({"error": "Producto no encontrado"})

