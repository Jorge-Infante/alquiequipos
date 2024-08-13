from rest_framework import serializers
from applications.orders.models import Order,OrderDetail,OrderDetailHistory
from applications.products.api.serializers import ServiceSerializer

class OrderDetailHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetailHistory
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = OrderDetail
        fields = ['service','equipment_rented','equipment_delivered','created']

class OrderSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()
    order_details = OrderDetailSerializer(many=True, read_only=True, source='orderdetail_set')

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'created', 'order_details', 'history']

    def get_history(self, item):
        history = OrderDetailHistory.objects.filter(id_order=item.id)
        return OrderDetailHistorySerializer(history, many=True).data
