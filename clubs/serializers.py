from rest_framework import serializers
from .models import Club
from users.serializers import UserSerializer

class ClubSerializer(serializers.ModelSerializer):
    club_leader = UserSerializer(read_only=True)
    class Meta:
        model = Club
        fields = ['id', 'title', 'description', 'icon', 'club_leader']