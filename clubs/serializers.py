from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from users.models import User
from .models import Club, ClubJoinRequest
from users.serializers import UserSerializer


class ClubSerializer(serializers.ModelSerializer):
    club_leader = UserSerializer(read_only=True)
    club_leader_id = serializers.PrimaryKeyRelatedField(
        required=False, queryset=User.objects.all()
    )

    is_join_requested = serializers.BooleanField(default=False, read_only=True)
    is_join_request_approved = serializers.BooleanField(default=False, read_only=True)
    members_count = serializers.IntegerField(read_only=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        try:
            user = self.context["user"]

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
            "members_count",
            "is_approved",
            "is_join_requested",
            "is_join_request_approved",
            "created",
            "updated",
        ]


class ClubJoinRequestSerializer(serializers.ModelSerializer):

    club = ClubSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ClubJoinRequest
        fields = ["id", "club", "user", "is_approved", "created", "updated"]
