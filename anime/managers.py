from django.db import models
from django.db.models import Count

class AnimeQuerySet(models.QuerySet):
    def get_latest_anime(self):
        return self.order_by('-time')

    def get_anime_by_country(self, country):
        return self.filter(country_of_origin=country)

    def get_top_anime(self):
        return self.all().annotate(rating = Count('ratings__score')).order_by('-rating') #gives the anime with most ratings, cant figure how to give with the specific "masterpiece" rating

class AnimeManager(models.Manager):
    def get_queryset(self):
        return AnimeQuerySet(self.model, using=self._db)

    def get_latest_anime(self):
        return self.get_queryset().get_latest_anime()

    def get_anime_by_country(self, country):
        return self.get_queryset().get_anime_by_country(country)

    def get_top_anime(self):
        return self.get_queryset().get_top_anime()


class CommentQuerySet(models.QuerySet):
    def get_latest_comments(self):
        return self.order_by('-time')

class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)


class RatingQuerySet(models.QuerySet):
    def get_anime_by_rating(self, rating):
        return self.filter(score=rating)

class RatingManager(models.Manager):
    def get_queryset(self):
        return RatingQuerySet(self.model, using=self._db)

    def get_anime_by_rating(self, rating):
        return self.get_queryset().get_anime_by_rating(rating)
    