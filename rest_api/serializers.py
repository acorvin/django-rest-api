from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Testing API view"""
    name = serializers.CharField(max_length=10)