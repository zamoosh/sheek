from rest_framework import serializers

from projects.models import *
from client.serializer import UserSafeSerializer


class JobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobField
        fields = '__all__'


class JobFieldTagSerializer(serializers.ModelSerializer):
    jobField_parent = serializers.SerializerMethodField()
    jobField_parent_parent = serializers.SerializerMethodField()

    class Meta:
        model = JobField
        fields = '__all__'

    @staticmethod
    def get_jobField_parent(obj):
        return obj.parent.title

    @staticmethod
    def get_jobField_parent_parent(obj):
        return obj.parent.parent.title


class LowProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
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


class UserJobfieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobField
        fields = '__all__'


class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserState
        fields = '__all__'
