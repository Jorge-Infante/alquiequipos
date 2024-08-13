from rest_framework.routers import DefaultRouter
from applications.orders.api.views import *

router_order = DefaultRouter()
router_order.register(
    prefix='orders', basename='orders', viewset=OrderViewSet
)