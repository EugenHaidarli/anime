from django.db import models
from django.db.models.fields import BooleanField, CharField, FilePathField, IntegerField
from django.db.models.fields.related import ForeignKey
from django_countries.fields import CountryField
from django.conf import settings
from rest_framework.fields import FileField, ImageField
from .managers import AnimeManager, CommentManager, RatingManager

class Anime(models.Model):
    name = CharField(max_length=100)
    owner = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        null=True, 
        on_delete=models.SET_NULL ,
        related_name='animes'
    )
    is_series = BooleanField(default=True)
    episodes = IntegerField(null=True)
    cover = models.ImageField(null=True, blank=True)
    time = models.DateField(null=True, auto_now_add=True)
    objects = AnimeManager()

    class CountryChoice(models.TextChoices):
        JAPAN = 'japan', 'Japan'
        SOUTH_KOREA = 'south korea', 'South Korea'
        CHINA = 'china', 'China'
        USA = 'usa', 'USA'

    country_of_origin = models.CharField("Country of origin", max_length=20, choices=CountryChoice.choices, blank=True)
    
    def __str__(self):
        return self.name

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
    objects = CommentManager()

    def __str__(self):
        return self.content

class Rating(models.Model):
    anime = ForeignKey(Anime, on_delete=models.CASCADE, related_name='ratings')
    owner = models.ForeignKey( 
        settings.AUTH_USER_MODEL, 
        null=True, 
        on_delete=models.SET_NULL,
        related_name='ratings' 
    )
    objects = RatingManager()

    class RatingChoice(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        BAD = "bad", "Bad"
        OKAY = "okay", "Okay"
        GOOD = "good", "Good"
        NICE = "nice", "Nice"
        MASTERPIECE = "masterpiece", "Masterpiece"

    score = models.CharField("Anime Score",max_length=20, choices=RatingChoice.choices, default=RatingChoice.UNSPECIFIED)

    def __str__(self):
        return self.score