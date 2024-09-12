from rest_framework.viewsets import ModelViewSet
from applications.products.models import Product, Measure
from applications.products.api.serializers import ProductSerializer, MeasureSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MeasureViewSet(ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
