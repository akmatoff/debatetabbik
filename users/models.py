from django.contrib.auth.models import AbstractUser
from django.db import models
from clubs.models import Club


class User(AbstractUser):
    club = models.ForeignKey(
        Club, related_name="users", on_delete=models.PROTECT, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.username
