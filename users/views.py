from rest_framework import generics, permissions
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .models import User
from .serializers import UserSerializer
from clubs.models import Club
from clubs.serializers import ClubSerializer
import requests


class UsersList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserData(APIView):
    @extend_schema(
        responses={200: UserSerializer},
        description="Get current user data",
    )
    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        user = request.user

        print("USER")
        print(user)

        social = user.social_auth.get(provider="google-oauth2")

        res = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            params={"access_token": social.extra_data["access_token"]},
        )

        userdata = res.json()

        user.avatar = userdata["picture"]
        user.save()

        print("USERDATA")
        print(userdata)

        if user.club is not None:
            club = Club.objects.get(pk=user.club.id)

            if club is not None:

                club_serializer = ClubSerializer(
                    club, context={"user": request.user, "request": request}
                )

                return Response({"user": serializer.data, "club": club_serializer.data})

        return Response({"user": serializer.data, "club": None})


@api_view(["GET"])
def google_auth_callback(request):
    user = request.user

    print("USER")
    print(user)

    social = user.social_auth.get(provider="google-oauth2")

    res = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        params={"access_token": social.extra_data["access_token"]},
    )

    userdata = res.json()

    user.avatar = userdata["picture"]
    user.save()

    print("USERDATA")
    print(userdata)

    return Response(
        {"message": "Authenticated successfully!"}, status=status.HTTP_200_OK
    )
