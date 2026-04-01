# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'groups', views.GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_id>/comments/',
        views.CommentViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='post-comments'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        views.CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='comment-detail'
    ),
]
