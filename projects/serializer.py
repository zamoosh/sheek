from rest_framework import serializers

from projects.models import *


class JobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobField
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
