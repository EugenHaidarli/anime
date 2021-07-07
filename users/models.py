from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import ugettext_lazy as _
from anime.models import Anime
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    watched_list = models.ManyToManyField(Anime, blank=True, related_name= 'animes')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def add_anime_to_watched_list(self, anime):
        return self.watched_list.add(anime)

    def remove_anime_from_watched_list(self, anime):
        return self.watched_list.remove(anime)

    def __str__(self):
        return self.email
