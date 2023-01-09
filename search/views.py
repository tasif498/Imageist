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
import urllib


class search_api(APIView):
    @csrf_exempt
    def get(self, request):
        # print(request)
        query = request.query_params.get('q')
        query = urllib.parse.unquote_plus(query)
        # print('Got Query:',query)
        if query:
            products = Products.objects.all()
            if query != 'all':
                # print('Got Query:',query)
                terms = query.split()
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
            product_serializer = ProductSerializer(products, many=True)
            # print(products)
            # print('===================================')
            return JsonResponse(product_serializer.data, safe=False)
        return JsonResponse('Please provide a query.', safe=False)

    @csrf_exempt
    def post(self, request):
        product = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed To Add', safe=False)

class report_api(APIView):
    @csrf_exempt
    def get(self,request):
        link = request.query_params.get('l')
        link = urllib.parse.unquote_plus(link)
        if link:
            print('Link',link)
            return JsonResponse('Reported Successfully',safe=False)
        return JsonResponse('Failed to Report',safe=False)
            