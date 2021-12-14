from rest_framework import serializers

from state.models import State


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
