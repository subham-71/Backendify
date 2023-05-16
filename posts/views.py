from django.shortcuts import render

from authentication.jwt import JWTAuthentication
from .models import Post
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import response, status, permissions


# Create your views here.

class selectedView(ListCreateAPIView):
    lookup_url_kwarg = "chapterName"
    serializer_class = PostSerializer

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Post.objects.filter(chapterName=uid)
        return queryset


class idView(APIView):

    def get(self, request, id):
        queryset = Post.objects.get(id=id)
        serializer = PostSerializer(queryset)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def put(self, request, id):

        if (JWTAuthentication.authenticate(self, request)):
            queryset = Post.objects.get(id=id)
            serializer = PostSerializer(queryset, data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Authentication Failed", status=status.HTTP_400_BAD_REQUEST)


class LikesDislikesView(APIView):

    def get(self, request, id):
        queryset = Post.objects.get(id=id)
        serializer = PostLikeDislikeSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):

        queryset = Post.objects.get(id=id)
        serializer = PostLikeDislikeSerializer(queryset, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class PostView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
    
class DeletePostView(APIView):

    def get(self, request, id):

        if (JWTAuthentication.authenticate(self, request)):
            print(id)
            queryset = Post.objects.get(id=id)
            Post.delete(queryset)
                
            return Response("post deleted", status=status.HTTP_200_OK)
            # return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Authentication Failed", status=status.HTTP_400_BAD_REQUEST)
