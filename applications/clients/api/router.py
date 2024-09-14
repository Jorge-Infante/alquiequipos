from rest_framework.routers import DefaultRouter
from applications.clients.api.views import *

router_client = DefaultRouter()
router_client.register(
    prefix='clients', basename='clients', viewset=ClientViewSet
)
