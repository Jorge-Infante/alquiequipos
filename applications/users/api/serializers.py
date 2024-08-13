from rest_framework import serializers
from applications.users.models import User
from django.contrib.auth.models import Group, Permission
    
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        group = Group.objects.create(**validated_data)
        for permission_data in permissions_data:
            permission = Permission.objects.get(codename=permission_data['codename'])
            group.permissions.add(permission)
        return group

    def update(self, instance, validated_data):
        permissions_data = validated_data.pop('permissions')
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        # Clear existing permissions
        instance.permissions.clear()
        for permission_data in permissions_data:
            permission = Permission.objects.get(codename=permission_data['codename'])
            instance.permissions.add(permission)
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        