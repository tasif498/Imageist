from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db.models import Q
from search.models import Products
from search.serializers import ProductSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class search_api(APIView):
    @csrf_exempt
    def get(self, request):
        query=request.query_params.get('q')
        if query:
            print(query)
            products=Products.objects.all()
            terms =query.split()
            for term in terms:
                products = products.filter(
                    Q(title__contains=term) |
                    Q(description__contains=term) |
                    Q(colors__contains=term) |
                    Q(gender__contains=term) |
                    Q(images__contains=term) |
                    Q(price__contains=term) |
                    Q(product_link__contains=term) |
                    Q(sizes__contains=term) |
                    Q(sku__contains=term) |
                    Q(type__contains=term)
                )
            product_serializer=ProductSerializer(products,many=True)
            print(products)
            return JsonResponse(product_serializer.data,safe=False)
        return JsonResponse('Please provide a query.')
    @csrf_exempt
    def post(self,request):
        product=JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed To Add',safe=False)
# @csrf_exempt
# def productApi(request, q=0):

    # if request.method=='GET':
    #     products=Products.objects.all()
    #     products_serializer=ProductSerializer(products,many=True)
    #     return JsonResponse(products_serializer.data,safe=False)
    # elif request.method=='POST':
    #     product_data=JSONParser().parse(request)
    #     print(product_data)
    #     del product_data['_id']
    #     products_serializer=ProductSerializer(data=product_data)
    #     if products_serializer.is_valid():
    #         products_serializer.save()
    #         return JsonResponse('Added Successfully',safe=False)
    #     return JsonResponse('Failed to Add',safe=False)
    # elif request.method=='PUT':
    #     product_data=JSONParser.parse(request)
    #     product=Products.objects.get(_id=product_data['_id'])
    #     products_serializer=ProductSerializer(product,data=product_data)
    #     if products_serializer.is_valid():
    #         products_serializer.save()
    #         return JsonResponse('Updated Successfully', safe=False)
    #     return JsonResponse('Failed to Update')
    # elif request.method=='DELETE':
    #     product=Products.objects.get(_id=id)
    #     product.delete()
    #     return JsonResponse('Deleted Successfully',safe=False)