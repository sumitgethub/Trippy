
from rest_framework import serializers
from .models import Role, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'role','otp']
        extra_kwargs = {'otp': {'write_only': True}}


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number',]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'