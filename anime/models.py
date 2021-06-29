from django.db import models
from django.db.models.fields import BooleanField, CharField, FilePathField, IntegerField
from django.db.models.fields.related import ForeignKey
from django_countries.fields import CountryField

class Anime(models.Model):
    name = CharField(max_length=100)
    owner = models.ForeignKey('auth.User', null=True, related_name='anime', on_delete=models.CASCADE)
    # country_of_origin = CountryField("Country of origin", blank=True)
    is_series = BooleanField(default=True)
    episodes = IntegerField(blank=True)
    cover = FilePathField()

class Comment(models.Model):
    anime = ForeignKey(Anime, on_delete=models.CASCADE, related_name='animes')
    owner = models.ForeignKey('auth.User', null=True, related_name='comments', on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, blank=True)

class Rating(models.Model):
    anime = ForeignKey(Anime, on_delete=models.CASCADE, related_name='anime')
    owner = models.ForeignKey('auth.User', null=True, related_name='ratings', on_delete=models.CASCADE)

    class RatingChoice(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        BAD = "bad", "Bad"
        OKAY = "okay", "Okay"
        GOOD = "good", "Good"
        NICE = "nice", "Nice"
        MASTERPIECE = "masterpiece", "Masterpiece"

    score = models.CharField("Anime Score",max_length=20, choices=RatingChoice.choices, default=RatingChoice.UNSPECIFIED)
