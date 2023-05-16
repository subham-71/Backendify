from django.shortcuts import render
from authentication.jwt import JWTAuthentication
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.views import APIView
from authentication import serializers
from authentication.serializers import *
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from .models import User, MyUserManager
from rest_framework.response import *


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(GenericAPIView):

    serializer_class = UpdateProfileSerializer

    def put(self, request, email):
        if (JWTAuthentication.authenticate(self, request)):
            queryset = User.objects.get(email=email)
            serializer = UpdateProfileSerializer(queryset, data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response("Authentication Failed")


class SuperRegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = SuperRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(email=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            response1 = {
                "name": user.name, 'serializer': serializer.data}
            return Response(response1, status=status.HTTP_200_OK)
        return Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):

    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.get(email=email)
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user.set_password(password)
            user.save()

            return Response("Password changed successfully", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):

    def post(self, request):
        if (JWTAuthentication.authenticate(self, request)):
            email = request.data.get('email', None)

            user = User.objects.get(email=email)
            serializer = DeleteUserSerializer(data=request.data)

            if serializer.is_valid():
                user.delete()
                return Response("User deleted", status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Authentication Failed")


class UserEmailView(APIView):

    def get(self, request, email):
        queryset = User.objects.get(
            email=email)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)


class AllUsersView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
