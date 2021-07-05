from rest_framework import serializers
from .models import Anime, Comment, Rating
from users.models import CustomUser

class UserCommentSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, comment):
        return comment.comments.count()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'comment_count']


class UserRatingSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()

    def get_rating_count(self, rating):
        return rating.ratings.count()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'rating_count']


class UserAnimeSerializer(serializers.ModelSerializer):
    anime_count = serializers.SerializerMethodField()

    def get_anime_count(self, anime):
        return anime.animes.count()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'anime_count']


class CommentSerializer(serializers.ModelSerializer):
    owner = UserCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'anime', 'owner', 'time', 'content']


class RatingSerializer(serializers.ModelSerializer):
    owner = UserRatingSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'anime', 'owner', 'score']


class AnimeSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    owner = UserAnimeSerializer(read_only=True)
    cover = serializers.ImageField() # gotta research more about using imagefield

    class Meta:
        model = Anime
        fields = ['id', 'name', 'owner', 'is_series', 'episodes', 'cover', 'comments', 'ratings']


class UserSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only = True, many=True)
    ratings = RatingSerializer(read_only=True, many=True)
    animes = AnimeSerializer(read_only=True, many=True)
    

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'watched_list', 'animes', 'comments', 'ratings']
