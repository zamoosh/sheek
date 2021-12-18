from rest_framework import serializers


class JobFieldViewDto(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    status = serializers.BooleanField()
    description = serializers.CharField()
    parent = serializers.IntegerField()


class ProjectCreateDto(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    owner = serializers.IntegerField()
    user_jobField = serializers.IntegerField(required=False)
    state = serializers.IntegerField()


class ProjectViewDto(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    owner = serializers.IntegerField()
    user_jobField = serializers.IntegerField()
    state = serializers.IntegerField()
    rate = serializers.IntegerField()
    status = serializers.BooleanField()
    status_jobField_user = serializers.IntegerField()
