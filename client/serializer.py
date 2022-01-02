from django.contrib.auth.models import Permission

from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    parent_state = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']

    @staticmethod
    def get_parent_state(obj):
        if obj.state:
            if obj.state.parent:
                return obj.state.parent.id
        return None


class UserSafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image' ]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
