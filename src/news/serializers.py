from datetime import datetime

from rest_framework import serializers

from .models import News


class NewsReadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="news_id")

    class Meta:
        model = News
        fields = (
            "stock",
            "category",
            "datetime",
            "headline",
            "id",
            "image",
            "related",
            "source",
            "summary",
            "url",
        )
        read_only_fields = fields

class NewsCreateSerializer(serializers.ModelSerializer):
    stock = serializers.CharField(write_only=True)
    category = serializers.CharField(write_only=True, allow_blank=True)
    datetime = serializers.IntegerField(write_only=True)
    headline = serializers.CharField(write_only=True, allow_blank=True)
    id = serializers.IntegerField(source="news_id", write_only=True)
    image = serializers.URLField(write_only=True, allow_blank=True)
    related = serializers.CharField(write_only=True, allow_blank=True)
    source = serializers.CharField(write_only=True, allow_blank=True)
    summary = serializers.CharField(write_only=True, allow_blank=True)
    url = serializers.URLField(write_only=True, allow_blank=True)

    def validate_datetime(self, value):
        return datetime.fromtimestamp(value)

    class Meta:
        model = News
        fields = (
            "stock",
            "category",
            "datetime",
            "headline",
            "id",
            "image",
            "related",
            "source",
            "summary",
            "url",
        )


class CreateNewsInRangeSerializer(serializers.Serializer):
    from_date = serializers.DateField(required=True)
    to_date = serializers.DateField(required=True)
