from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "club_id", "email"]

    def to_representation(self, instance):
        club_id = None

        if instance.club_id:
            club_id = instance.club_id

        return {
            "id": instance.id,
            "username": instance.username,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "club_id": club_id,
        }
