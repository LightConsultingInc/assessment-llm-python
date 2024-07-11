from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    messages = serializers.ListField(child=serializers.DictField())