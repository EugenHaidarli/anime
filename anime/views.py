from rest_framework import serializers, viewsets
from .models import Anime, Comment, Rating
from .serializers import AnimeSerializer, CommentSerializer, RatingSerializer, UserSerializer
from rest_framework import permissions
from users.models import CustomUser

class AnimeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment viewset
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]