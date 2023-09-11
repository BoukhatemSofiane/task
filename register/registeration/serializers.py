from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'user_type', 'name', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            name=validated_data['name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user