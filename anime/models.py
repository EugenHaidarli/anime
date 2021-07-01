from django.db import models
from django.db.models.fields import BooleanField, CharField, FilePathField, IntegerField
from django.db.models.fields.related import ForeignKey
from django_countries.fields import CountryField
from django.conf import settings
from rest_framework.fields import FileField, ImageField

class Anime(models.Model):
    name = CharField(max_length=100)
    owner = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        null=True, 
        on_delete=models.SET_NULL ,
        related_name='animes'
    )
    # country_of_origin = CountryField("Country of origin", blank=True)
    is_series = BooleanField(default=True)
    episodes = IntegerField(blank=True)
    cover = ImageField()

class Comment(models.Model):
    anime = ForeignKey(Anime, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='comments' 
    )
    time = models.TimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, blank=True)

class Rating(models.Model):
    anime = ForeignKey(Anime, on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='ratings' 
    )

    class RatingChoice(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        BAD = "bad", "Bad"
        OKAY = "okay", "Okay"
        GOOD = "good", "Good"
        NICE = "nice", "Nice"
        MASTERPIECE = "masterpiece", "Masterpiece"

    score = models.CharField("Anime Score",max_length=20, choices=RatingChoice.choices, default=RatingChoice.UNSPECIFIED)
