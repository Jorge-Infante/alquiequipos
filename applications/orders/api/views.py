from rest_framework.viewsets import ModelViewSet
from applications.orders.models import Order
from applications.orders.api.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer