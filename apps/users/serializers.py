from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'created_at']
        read_only_fields = ['created_at']

class UserCreateSerializer(serializer.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirm', 'profile_picture']
        extra_kwargs = {
            'password': {'wrote_only': True}
        }

    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)