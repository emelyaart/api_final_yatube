from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets

from .models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        group_id = self.request.query_params.get('group', None)

        if group_id is not None:
            group = get_object_or_404(Group, pk=group_id)
            queryset = group.posts.all()
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(
            author=self.request.user,
            post=post
        )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']

    def get_queryset(self):
        user = self.request.user
        queryset = user.following.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
