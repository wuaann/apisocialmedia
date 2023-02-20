from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('users', views.UserViewSet, 'user')
router.register('profile', views.PostUserViewser, 'profile')



urlpatterns = [
    path('', include(router.urls)),
    path('oauth2_info/', views.AuthInfo.as_view())
]


