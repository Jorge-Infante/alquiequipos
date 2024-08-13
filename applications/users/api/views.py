from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from . serializers import UserSerializer,PermissionSerializer,GroupSerializer

from applications.users.models import User
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.hashers import make_password

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class UserApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self,request,*args, **kwargs):
        request.data['password'] = make_password(request.data['password'] )
        return super().create(request,*args, **kwargs)
    
    def update(self,request,*args, **kwargs):
        if 'password' in request.data:
            request.data['password'] = make_password(request.data['password'] )
        else:
            request.data['password'] = request.user.password
        return super().update(request,*args, **kwargs)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)