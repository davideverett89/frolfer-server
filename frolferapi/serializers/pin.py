from rest_framework import serializers
from frolferapi.models import Pin

class PinSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf course pins.

    Arguments:
        serializers
    """
    class Meta:
        model = Pin
        fields = (
            'id',
            'label',
            'par',
            'distance',
            'hole_id',
            'active'
        )