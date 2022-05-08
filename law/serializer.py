from rest_framework import serializers
from law.models import *


class LawCategory(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class RuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'



