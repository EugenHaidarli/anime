from django.db.models import manager, query
from rest_framework import serializers, viewsets
from .models import Anime, Comment, Rating
from .serializers import AnimeSerializer, CommentSerializer, RatingSerializer, UserSerializer
from rest_framework import permissions
from users.models import CustomUser
from rest_framework.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['get'], url_path='rated')
    def top_rated_animes(self, request):
        query = self.queryset.get_top_anime()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='last')
    def last_made_anime(self, request, size=5):
        query = self.queryset.get_latest_anime(size)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='country')
    def anime_by_country(self, request, country="japan"):
        query = self.queryset.get_anime_by_country(country)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='watched')
    def top_watched_anime(self, request):
        query = self.queryset.get_top_watched_anime()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], url_path='top')
    def top_users(self, request):
        query = self.queryset.get_top_users()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Anime Comments viewset
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], url_path='latest')
    def latest_comment(self, request, size=5):
        query = self.queryset.get_latest_comments(size)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

class RatingViewSet(viewsets.ModelViewSet):
    """
    Anime Ratings viewset
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], url_path='score')
    def anime_by_score(self, request, score='masterpiece'):
        query = self.queryset.get_anime_by_rating(score)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)


