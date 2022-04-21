
from rest_framework import serializers
from api.Model.Message import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        field = ('msg', 'status')