from rest_framework import serializers


class JobFieldViewDto(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    status = serializers.BooleanField()
    description = serializers.CharField()
    parent = serializers.IntegerField()
