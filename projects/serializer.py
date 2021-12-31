from rest_framework import serializers

from projects.models import *


class JobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobField
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    jobField = serializers.SerializerMethodField()
    jobField_parent = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    @staticmethod
    def get_jobField(obj):
        return obj.jobField.title

    @staticmethod
    def get_jobField_parent(obj):
        return obj.jobField.parent.title
