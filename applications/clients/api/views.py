from rest_framework.viewsets import ModelViewSet
from applications.clients.models import Client
from applications.clients.api.serializers import ClientSerializer

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer