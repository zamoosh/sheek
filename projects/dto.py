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
    user_jobField = serializers.IntegerField(required=False)
    jobField = serializers.IntegerField()
    state = serializers.IntegerField()


class ProjectCreateCommentDto(serializers.Serializer):
    comment = serializers.CharField(required=False)
    rate = serializers.IntegerField()


class ProjectViewDto(serializers.Serializer):
    title = serializers.CharField()
    jobField = serializers.IntegerField()
    description = serializers.CharField()
    owner = serializers.IntegerField()
    user_jobField = serializers.IntegerField()
    state = serializers.IntegerField()
    rate = serializers.IntegerField()
    status = serializers.BooleanField()
    status_jobField_user = serializers.IntegerField()


class ProjectViewCommentDto(serializers.Serializer):
    title = serializers.CharField()
    jobField = serializers.IntegerField()
    description = serializers.CharField()
    owner = serializers.IntegerField()
    user_jobField = serializers.IntegerField()
    state = serializers.IntegerField()
    rate = serializers.IntegerField()
    status = serializers.BooleanField()
    status_jobField_user = serializers.IntegerField()
    comment = serializers.CharField()
