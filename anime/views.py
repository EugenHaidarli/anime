from rest_framework import viewsets
from .models import Anime, Comment, Rating
from .serializers import AnimeSerializer, CommentSerializer, RatingSerializer
from rest_framework import permissions

class AnimeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
