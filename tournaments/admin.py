from django.contrib import admin
from .models import (
    Tournament,
    TournamentJoinRequest,
    TournamentJudge,
    TournamentJudgePoint,
    TournamentRoom,
    TournamentRoomTeam,
    TournamentRound,
    TournamentRoundPoint,
    TournamentTeam,
    TournamentUserSpeakerPoint,
)


class TournamentsAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "icon")


class TournamentJoinRequestAdmin(admin.ModelAdmin):
    list_display = ("team_title", "is_approved", "first_speaker", "second_speaker")


class TournamentTeamAdmin(admin.ModelAdmin):
    list_display = ("title", "tournament", "first_speaker", "second_speaker")


class TournamentJudgeAdmin(admin.ModelAdmin):
    list_display = ("user", "tournament", "is_main")


class TournamentUserSpeakerPointAdmin(admin.ModelAdmin):
    list_display = ("user", "tournament", "speaker_points")


class TournamentJudgePointAdmin(admin.ModelAdmin):
    list_display = ("judge", "tournament", "points")


class TournamentRoundAdmin(admin.ModelAdmin):
    list_display = ("tournament", "round", "is_closed")


class TournamentRoundPointAdmin(admin.ModelAdmin):
    list_display = ("team", "round", "points")


class TournamentRoomAdmin(admin.ModelAdmin):
    list_display = ("tournament", "judge", "room")


class TournamentRoomTeamAdmin(admin.ModelAdmin):
    list_display = ("team", "room", "position")


admin.site.register(Tournament, TournamentsAdmin)
admin.site.register(TournamentJoinRequest, TournamentJoinRequestAdmin)
admin.site.register(TournamentTeam, TournamentTeamAdmin)
admin.site.register(TournamentJudge, TournamentJudgeAdmin)
admin.site.register(TournamentUserSpeakerPoint, TournamentUserSpeakerPointAdmin)
admin.site.register(TournamentJudgePoint, TournamentJudgePointAdmin)
admin.site.register(TournamentRound, TournamentRoundAdmin)
admin.site.register(TournamentRoundPoint, TournamentRoundPointAdmin)
admin.site.register(TournamentRoom, TournamentRoomAdmin)
admin.site.register(TournamentRoomTeam, TournamentRoomTeamAdmin)
