from rest_framework import serializers
from .user import UserSerializer

from frolferapi.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf players.

    Arguments:
        serializers
    """

    user = UserSerializer()
    class Meta:
        model = Player
        fields = (
            'id',
            'user',
            'rounds_played'
        )