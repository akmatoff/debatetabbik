from django.db import models
from django.utils import timezone


class Club(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to="club_icons/", null=True)
    club_leader = models.ForeignKey(
        "users.User", related_name="club_leader", on_delete=models.PROTECT
    )
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ClubJoinRequest(models.Model):
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    user = models.ForeignKey(
        "users.User", related_name="club_join_requests", on_delete=models.PROTECT
    )
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
