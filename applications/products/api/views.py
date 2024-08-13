from rest_framework.viewsets import ModelViewSet
from applications.products.models import Product
from applications.products.api.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer