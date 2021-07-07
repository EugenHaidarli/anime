from django.db import models
from django.db.models import Count, Q

class AnimeQuerySet(models.QuerySet):
    def get_latest_anime(self, size):
        return self.order_by('-time')[:size]

    def get_anime_by_country(self, country):
        return self.filter(country_of_origin=country)

    def get_top_anime(self):
        return self.all().annotate(rating = Count('ratings__score', filter=Q(ratings__score="masterpiece"))).order_by('-rating') #gives the anime with most ratings, cant figure how to give with the specific "masterpiece" rating

    def get_top_watched_anime(self):
        return self.all().annotate(anime = Count('animes')).order_by('-anime')

class AnimeManager(models.Manager):
    def get_queryset(self):
        return AnimeQuerySet(self.model, using=self._db)

    def get_latest_anime(self, size=5):
        return self.get_queryset().get_latest_anime(size)

    def get_anime_by_country(self, country):
        return self.get_queryset().get_anime_by_country(country)

    def get_top_anime(self):
        return self.get_queryset().get_top_anime()

    def get_top_watched_anime(self):
        return self.get_queryset().get_top_watched_anime()

    


class CommentQuerySet(models.QuerySet):
    def get_latest_comments(self, size):
        return self.order_by('-time')[:size]

class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

    def get_latest_comments(self, size=5):
        return self.get_queryset().get_latest_comments(size)


class RatingQuerySet(models.QuerySet):
    def get_anime_by_rating(self, rating):
        return self.filter(score=rating)

class RatingManager(models.Manager):
    def get_queryset(self):
        return RatingQuerySet(self.model, using=self._db)

    def get_anime_by_rating(self, rating):
        return self.get_queryset().get_anime_by_rating(rating)
    