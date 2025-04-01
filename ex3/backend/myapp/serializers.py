from rest_framework import serializers
from .models import User, Preference

class PreferenceSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='preference')
    class Meta:
        model = Preference
        fields = ['value']

class UserSerializer(serializers.ModelSerializer):
    preferences = PreferenceSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'affiliate', 'preferences']