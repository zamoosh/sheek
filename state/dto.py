from rest_framework import serializers


class ProvinceViewDto(serializers.Serializer):
    status = serializers.BooleanField()
    title = serializers.CharField()
    parent = serializers.IntegerField()
