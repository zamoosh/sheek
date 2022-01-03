from rest_framework import serializers

from projects.models import UserJobField


class ExpertSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    jobField = serializers.SerializerMethodField()
    owner_first = serializers.SerializerMethodField()
    owner_last = serializers.SerializerMethodField()

    class Meta:
        model = UserJobField
        fields = '__all__'

    @staticmethod
    def get_state(obj):
        return obj.state.title

    @staticmethod
    def get_owner_first(obj):
        return obj.owner.first_name

    @staticmethod
    def get_owner_last(obj):
        return obj.owner.last_name

    @staticmethod
    def get_jobField(obj):
        return obj.jobField.title

    @staticmethod
    def get_description(obj):
        return obj.UserJobField.description


class UserJobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobField
        fields = '__all__'
