from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view

# GET list of tutorials, POST a new tutorial, DELETE all tutorials
@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    # retrieve all products/find by title from MongoDB database
    if request.method == 'GET':
        products = Product.objects.all()
        title = request.GET.get('title', None)

        if title is not None:
            products = products.filter(title__icontains=title)

        products_serializer = ProductSerializer(products, many=True)

        # safe = False for objects serialization
        return JsonResponse(products_serializer.data, safe=False)

    # create and save a new product
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)

        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete all products from the database
    elif request.method == 'DELETE':
        count = Product.objects.all().delete()

        return JsonResponse({'message': '{} Product were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# GET / PUT / DELETE tutorial by ‘id’
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)

        # find a single product with an id
        if request.method == 'GET':
            product_serializer = ProductSerializer(product)
            return JsonResponse(product_serializer.data)

        # update a product by the id in the request
        elif request.method == 'PUT':
            product_data = JSONParser().parse(request)
            product_serializer = ProductSerializer(product, data=product_data)

            if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse(product_serializer.data)

            return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete a product with the specified id
        elif request.method == 'DELETE':
            product.delete()
            return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

# GET all published products
@api_view(['GET'])
def product_list_posted(request):
    products = Product.objects.filter(published=True)

    # find all products with published = True:
    if request.method == 'GET':
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
