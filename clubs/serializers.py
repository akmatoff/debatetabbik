from rest_framework import serializers
from .models import Club, ClubJoinRequest
from users.serializers import UserSerializer


class ClubSerializer(serializers.ModelSerializer):
    club_leader = UserSerializer(read_only=True)
    club_leader_id = serializers.IntegerField(write_only=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        user = self.context["user"]

        try:
            user_join_request = user.club_join_requests.get(club=instance.id)

            ret["is_join_requested"] = user_join_request is not None
            ret["is_join_request_approved"] = user_join_request.is_approved

        except:
            print("No join request")
            ret["is_join_requested"] = False
            ret["is_join_request_approved"] = False

        ret["members_count"] = len(instance.users.all())

        return ret

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
