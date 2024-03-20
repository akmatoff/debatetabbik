from django.db import models

class Club(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to='club_icons/', null=True)
    club_leader = models.ForeignKey('users.User', related_name="club_leader", on_delete=models.PROTECT)

    def __str__(self):
        return self.title