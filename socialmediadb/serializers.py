from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar', 'cover_pic']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'user', 'post_content',
                  'img', 'active']

    def create(self, validated_data):
        post = Post(**validated_data)
        post.active = True
        post.save()
        return post

