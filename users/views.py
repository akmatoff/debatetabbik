from rest_framework import generics, permissions
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from clubs.models import Club
from clubs.serializers import ClubSerializer
from social_django.utils import load_strategy


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

        if user.club is not None:
            club = Club.objects.get(pk=user.club.id)

            if club is not None:

                club_serializer = ClubSerializer(
                    club, context={"user": request.user, "request": request}
                )

                return Response({"user": serializer.data, "club": club_serializer.data})

        return Response({"user": serializer.data, "club": None})


@api_view(["POST"])
def google_auth_callback(request):
    strategy = load_strategy(request)
    user = request.user
    if user.is_authenticated and user.social_auth.exists():
        social = user.social_auth.get(provider="google-oauth2")
        access_token = social.extra_data["access_token"]

        userdata = strategy.backend.get_user_details(access_token)
        user.avatar = userdata["picture"]
        user.save()

    return Response(
        {"message": "Authenticated successfully!"}, status=status.HTTP_200_OK
    )


from django.shortcuts import redirect
