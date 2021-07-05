from rest_framework import serializers, viewsets
from .models import Anime, Comment, Rating
from .serializers import AnimeSerializer, CommentSerializer, RatingSerializer, UserSerializer
from rest_framework import permissions
from users.models import CustomUser
from rest_framework.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest

class AnimeViewSet(viewsets.ModelViewSet):
    """
    Anime viewset
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        return HttpResponseBadRequest("We dont delete art around this parts >:(")

class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Anime Comments viewset
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingViewSet(viewsets.ModelViewSet):
    """
    Anime Ratings viewset
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


