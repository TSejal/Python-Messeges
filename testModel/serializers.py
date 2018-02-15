from rest_framework import serializers
from testModel.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message