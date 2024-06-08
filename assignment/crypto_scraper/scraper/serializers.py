from rest_framework import serializers

class ScrapeRequestSerializer(serializers.Serializer):
    coins = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )
