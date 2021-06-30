from rest_framework import serializers
from .models import Anime, Comment, Rating

class AnimeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Anime
        fields = ['name', 'owner', 'is_series', 'episodes']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['anime', 'owner', 'time', 'content']

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['anime', 'owner', 'score']

