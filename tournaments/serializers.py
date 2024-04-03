from rest_framework import serializers
from .models import (
    Tournament,
    TournamentJoinRequest,
    TournamentTeam,
    TournamentJudge,
    TournamentUserSpeakerPoint,
    TournamentJudgePoint,
    TournamentRound,
    TournamentRoundPoint,
    TournamentRoom,
    TournamentRoomTeam,
    UserTournamentTeamInvitation,
)
from users.models import User


class TournamentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        required=False, queryset=User.objects.all()
    )

    class Meta:
        model = Tournament
        fields = "__all__"


class TournamentJoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentJoinRequest
        fields = "__all__"


class TournamentTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentTeam
        fields = "__all__"


class TournamentJudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentJudge
        fields = "__all__"


class TournamentUserSpeakerPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentUserSpeakerPoint
        fields = "__all__"


class TournamentJudgePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentJudgePoint
        fields = "__all__"


class TournamentRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRound
        fields = "__all__"


class TournamentRoundPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRoundPoint
        fields = "__all__"


class TournamentRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRoom
        fields = "__all__"


class TournamentRoomTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRoomTeam
        fields = "__all__"


class UserTournamentTeamInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTournamentTeamInvitation
        fields = "__all__"
