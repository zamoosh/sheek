from rest_framework import serializers


class LawCategoryViewDto(serializers.Serializer):
    title = serializers.CharField()


class RuleViewDto(serializers.Serializer):
    title = serializers.CharField()
    date = serializers.CharField()
    article = serializers.CharField()
    footnote = serializers.CharField()
    description = serializers.CharField()
    group = serializers.IntegerField()

