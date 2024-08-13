from rest_framework.routers import DefaultRouter
from applications.products.api.views import *

router_product = DefaultRouter()
router_product.register(
    prefix='products', basename='products', viewset=ProductViewSet
)