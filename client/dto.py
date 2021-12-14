from rest_framework import serializers


class TokenCreateDto(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.IntegerField(required=False)
    password = serializers.CharField(required=False)


class TokenViewDto(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class UserViewDto(serializers.Serializer):
    username = serializers.CharField()
    extra = serializers.JSONField()
    email = serializers.CharField()
    cellphone = serializers.CharField()
    image = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.BooleanField()


class UpdateProfileCreateDto(serializers.Serializer):
    image = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class Verify(serializers.Serializer):
    username = serializers.CharField()


class UpdateProfileCreateDto(serializers.Serializer):
    image = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


class UserInfoDto(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    has_password = serializers.BooleanField()


class UserInfoGetDto(serializers.Serializer):
    username = serializers.CharField()


class UserCreateAdminDto(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    cellphone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)


class UserUpdateAdminDto(serializers.Serializer):
    password = serializers.CharField(required=False)
    cellphone = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    id = serializers.IntegerField()


class PermissionsDto(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    codename = serializers.CharField()


class UserInfoDto(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    has_password = serializers.BooleanField()


class UserInfoGetDto(serializers.Serializer):
    username = serializers.CharField()


class UserGroupUpdateDto(serializers.Serializer):
    user_id = serializers.IntegerField()
    group_id = serializers.IntegerField()


class UserUpdatePermsDto(serializers.Serializer):
    id = serializers.IntegerField()
    permission = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100)
    )
