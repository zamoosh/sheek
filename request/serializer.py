from rest_framework import serializers

from projects.models import *


class ExpertSerializer(serializers.ModelSerializer):
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


class UserJobFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobField
        fields = '__all__'


