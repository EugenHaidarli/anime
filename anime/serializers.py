from rest_framework import serializers
from .models import Anime, Comment, Rating
from users.models import CustomUser


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'anime', 'owner', 'time', 'content']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'anime', 'owner', 'score']


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ['id', 'name', 'owner', 'is_series', 'episodes']


class UserSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only = True, many=True)
    ratings = RatingSerializer(read_only=True, many=True)
    animes = AnimeSerializer(read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'animes', 'comments', 'ratings']
