from rest_framework import serializers
from applications.products.models import Service, Product

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','measure','price','quantity','size']

        


        