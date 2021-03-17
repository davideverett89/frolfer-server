"""View module for handling requests about disc golf pins"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frolferapi.models import Pin

class Pins(ViewSet):
    """Frolfer disc golf course pins"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single disc golf pins.

        Returns:
            Response -- JSON serialized disc golf pins.
        """

        try:
            pin = Pin.objects.get(pk=pk)
            serializer = PinSerializer(pin, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all disc golf pins.

        Returns:
            Response -- JSON serialized list of all disc golf pins.
        """

        pins = Pin.objects.all()
        serializer = PinSerializer(
            pins, many=True, context={ 'request': request }
        )
        return Response(serializer.data)

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
            'length',
            'hole_id',
            'active'
        )
