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


class ProjectDto(serializers.Serializer):
    title = serializers.CharField()
    rate = serializers.IntegerField()
    status = serializers.BooleanField()
    TYPE = (
        (0, 'before confirm'),
        (1, 'progress'),
        (2, 'done'),
    )
    status_jobField_user = serializers.ChoiceField(choices=TYPE)
    description = serializers.CharField()
    owner = serializers.IntegerField()
    jobField = serializers.IntegerField()
    user_jobField = serializers.IntegerField()
    state = serializers.IntegerField()
    update_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()


class ConfirmDto(serializers.Serializer):
    id = serializers.IntegerField()
