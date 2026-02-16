from rest_framework import serializers
from .models import Registration
from django.contrib.auth.hashers import make_password


class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=100,
        error_messages={'required': 'Name is required',
                        'blank': 'Name is required'}
    )
    email = serializers.EmailField(
        error_messages={'required': 'Email is required',
                        'invalid': 'Enter a valid email address'}
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={'required': 'Password is required',
                        'blank': 'Password is required'}
    )
    # confirm_password = serializers.CharField(
    #     write_only=True,
    #     error_mesdef create(self, validated_data):
    #     """Hash password before saving"""
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return User.objects.create(**validated_data)sages={'required': 'Confirm Password is required'}
    # )

    def create(self, validated_data):
        """Hash password before saving"""
        validated_data['password'] = make_password(validated_data['password'])
        return Registration.objects.create(**validated_data)

    def validate_password(self, value):
        if len(value) < 0:
            raise serializers.ValidationError(
                "length of password must at least 8")
        return value
