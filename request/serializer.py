from rest_framework import serializers

from projects.models import UserJobField


class ExpertSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField
    jobField = serializers.SerializerMethodField

    class Meta:
        model = UserJobField
        fields = '__all__'

    @staticmethod
    def get_state(obj):
        return obj.state.title

    @staticmethod
    def get_jobField(obj):
        return obj.jobField.title
