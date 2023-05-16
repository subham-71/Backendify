from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostLikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['likes', 'dislikes', 'liked_users', 'disliked_users']
