from rest_framework import serializers

from projects.models import JobField


class JobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobField
        fields = '__all__'
