from rest_framework import serializers

from coverter.models import Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ("short_name", "rate_to_usd")

