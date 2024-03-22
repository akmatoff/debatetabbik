from rest_framework import generics, permissions
from rest_framework.views import APIView, Response
from .models import User
from .serializers import UserSerializer
from clubs.models import Club
from clubs.serializers import ClubSerializer


class UsersList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserData(APIView):
    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        if user.club:
            club = Club.objects.get(pk=user.club.id)

            club_serializer = ClubSerializer(club)

        return Response({"user": serializer.data, "club": club_serializer.data})
