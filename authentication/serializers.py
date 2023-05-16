from django.contrib.auth.models import User
from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email','organization', 'profile_pic']


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password','organization', 'profile_pic')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UpdateProfileSerializer (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'profile_pic' , 'organization')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SuperRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password','organization')

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    
class SuperLoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']


class ChangePasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')


class DeleteUserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('email')
