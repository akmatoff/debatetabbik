from django.db import models
from django.utils import timezone
from users.models import User


class Tournament(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="tournament_icons/", null=True)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, related_name="tournaments", on_delete=models.PROTECT
    )
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class TournamentJoinRequest(models.Model):
    first_speaker = models.ForeignKey(
        User, related_name="first_speaker_join_requests", on_delete=models.PROTECT
    )
    second_speaker = models.ForeignKey(
        User, related_name="second_speaker_join_requests", on_delete=models.PROTECT
    )
    tournament = models.ForeignKey(
        Tournament, related_name="join_requests", on_delete=models.PROTECT
    )
    team_title = models.CharField(max_length=255)
    is_approved = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.team_title


class TournamentTeam(models.Model):
    title = models.CharField(max_length=255)
    first_speaker = models.ForeignKey(
        User, related_name="first_speaker_teams", on_delete=models.PROTECT
    )
    second_speaker = models.ForeignKey(
        User, related_name="second_speaker_teams", on_delete=models.PROTECT
    )
    tournament = models.ForeignKey(
        Tournament, related_name="teams", on_delete=models.PROTECT
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class TournamentJudge(models.Model):
    user = models.ForeignKey(User, related_name="judges", on_delete=models.PROTECT)
    tournament = models.ForeignKey(
        Tournament, related_name="judges", on_delete=models.PROTECT
    )
    is_main = models.BooleanField(default=False)


class TournamentUserSpeakerPoint(models.Model):
    user = models.ForeignKey(
        User, related_name="speaker_points", on_delete=models.PROTECT
    )
    tournament = models.ForeignKey(
        Tournament, related_name="speaker_points", on_delete=models.PROTECT
    )
    speaker_ponits = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


class TournamentJudgePoint(models.Model):
    judge = models.ForeignKey(
        User, related_name="judge_points", on_delete=models.PROTECT
    )
    tournament = models.ForeignKey(
        Tournament, related_name="judge_points", on_delete=models.PROTECT
    )
    points = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


class TournamentRound(models.Model):
    tournament = models.ForeignKey(
        Tournament, related_name="rounds", on_delete=models.PROTECT
    )
    round = models.IntegerField()
    resolution = models.TextField()
    is_closed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


class TournamentRoundPoint(models.Model):
    team = models.ForeignKey(
        TournamentTeam, related_name="round_points", on_delete=models.PROTECT
    )
    round = models.ForeignKey(
        TournamentRound,
        related_name="round_points",
        on_delete=models.PROTECT,
    )
    points = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)


class TournamentRoom(models.Model):
    tournament = models.ForeignKey(
        Tournament, related_name="rooms", on_delete=models.PROTECT
    )
    judge = models.ForeignKey(User, related_name="rooms", on_delete=models.PROTECT)
    room = models.IntegerField()


class TournamentRoomTeam(models.Model):
    POSITION_CHOISES = [
        ("opening_government", "opening_government"),
        ("closing_government", "closing_government"),
        ("opening_opposition", "opening_opposition"),
        ("closing_opposition", "closing_opposition"),
    ]

    team = models.ForeignKey(
        TournamentTeam, related_name="room_teams", on_delete=models.PROTECT
    )
    room = models.ForeignKey(
        TournamentRoom, related_name="room_teams", on_delete=models.PROTECT
    )
    position = models.CharField(max_length=60, choices=POSITION_CHOISES)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
