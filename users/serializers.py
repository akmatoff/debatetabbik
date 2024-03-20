from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'club', 'email']

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "username": instance.username,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "email": instance.email,
            "club": {
                "id": instance.club.id,
                "title": instance.club.title,
                "description": instance.club.description,
                "rating": instance.club.rating,
                "icon": str(instance.club.icon),
                "club_leader_id": instance.club.club_leader_id
            }
        }