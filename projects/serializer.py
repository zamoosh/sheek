from rest_framework import serializers

from projects.models import *
from client.serializer import UserSafeSerializer


class JobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobField
        fields = '__all__'


class LowProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    jobField = serializers.SerializerMethodField()
    jobField_parent = serializers.SerializerMethodField()
    userdata = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    @staticmethod
    def get_jobField(obj):
        return obj.jobField.title

    @staticmethod
    def get_jobField_parent(obj):
        return obj.jobField.parent.title

    @staticmethod
    def get_userdata(obj):
        if obj.user_jobField:
            return UserSafeSerializer(obj.user_jobField.owner, many=False).data
        return {}
