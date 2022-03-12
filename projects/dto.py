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


class MessageCreateDto(serializers.Serializer):
    text = serializers.CharField()


class MessageViewDto(serializers.Serializer):
    created_at = serializers.DateTimeField()
    text = serializers.CharField()
    user_view = serializers.BooleanField()
    expert_view = serializers.BooleanField()
    project = serializers.IntegerField()
    owner = serializers.IntegerField()


class UserJobFielddViewDto(serializers.Serializer):
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    status = serializers.BooleanField()
    delete = serializers.BooleanField()
    status_comment = serializers.CharField()
    expiration = serializers.DateField()
    issue = serializers.DateField()
    jobField = serializers.IntegerField()
    owner = serializers.IntegerField()
    # state = serializers.ForeignKey(State, on_delete=serializers.CASCADE)
    description = serializers.CharField()
    inquiry_link = serializers.CharField()
    document_image = serializers.FileField()


class UserJobFieldCreateDto(serializers.Serializer):
    expiration = serializers.DateField()
    issue = serializers.DateField()
    jobField = serializers.IntegerField()
    description = serializers.CharField()
    inquiry_link = serializers.CharField()
    document_image = serializers.FileField()



class UserStateViewDto(serializers.Serializer):
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    userjobfield = serializers.IntegerField()
    state = serializers.IntegerField()
    status = serializers.BooleanField()


class UserStateCreateDto(serializers.Serializer):
    state_list = serializers.ListField(child=serializers.IntegerField())
