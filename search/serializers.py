from rest_framework import serializers
from search.models import Products
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):   
    class Meta:
        model=Products
        fields=('colors',	'description',	'gender',	'images',	'price',	'product_link'	,'sizes',	'sku',	'title',	'type')
