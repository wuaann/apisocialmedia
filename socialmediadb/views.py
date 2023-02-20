from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, status
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.views import APIView
from django.conf import settings


# Create your views here.

class UserViewSet(viewsets.ViewSet,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView,
                  generics.ListAPIView,
                  ):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser, ]

    @action(methods=['GET'], detail=False, url_path="current_user")
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser, ]
    queryset = Post.objects.filter(active=True)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


class PostUserViewser(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            post = post.filter(user_id__contains=q)

        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            post = post.filter(user_id=user_id)

        return post