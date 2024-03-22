from rest_framework import serializers
from .models import Club, ClubJoinRequest
from users.serializers import UserSerializer


class ClubSerializer(serializers.ModelSerializer):
    club_leader = UserSerializer(read_only=True)
    club_leader_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Club
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "rating",
            "club_leader",
            "club_leader_id",
            "is_approved",
            "created",
            "updated",
        ]


class ClubJoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubJoinRequest
        fields = "__all__"
