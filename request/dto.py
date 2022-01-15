from rest_framework import serializers


class UserJobFieldViewDto(serializers.Serializer):
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    status = serializers.BooleanField()
    delete = serializers.BooleanField()
    status_comment = serializers.CharField()
    experience = serializers.DateField()
    jobField = serializers.IntegerField()
    owner = serializers.IntegerField()
    state = serializers.IntegerField()
