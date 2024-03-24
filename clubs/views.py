from rest_framework import generics, permissions, status
from rest_framework.views import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Club, ClubJoinRequest
from users.models import User
from users.serializers import UserSerializer
from .serializers import ClubSerializer, ClubJoinRequestSerializer
from tabber_api.utils import parse_bool_query_param


class ClubsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ClubSerializer

    def get_queryset(self):
        queryset = Club.objects.all()
        is_approved = parse_bool_query_param(
            self.request.query_params.get("is_approved")
        )
        all_clubs = parse_bool_query_param(self.request.query_params.get("all_clubs"))

        queryset = queryset.filter(is_approved=True)

        if is_approved is not None:
            queryset = Club.objects.all().filter(is_approved=is_approved)

        if all_clubs:
            queryset = Club.objects.all()

        return queryset


class ClubDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if instance.club_leader.id == user.id:
            return super().update(request, *args, **kwargs)

        return Response(
            {"error": "No permission to edit."}, status=status.HTTP_403_FORBIDDEN
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if instance.club_leader.id == user.id:
            return super().delete(request, *args, **kwargs)

        return Response(
            {"error": "No permission to delete."}, status=status.HTTP_403_FORBIDDEN
        )


class ClubJoinRequestsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer


class ClubJoinRequestsDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer


# @pk - club id
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def request_to_join_club(request, pk):
    user = request.user

    try:
        club = Club.objects.get(pk=pk)

        join_request = ClubJoinRequest.objects.create(club=club, user=user)
        serializer = ClubJoinRequestSerializer(join_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        print(e)
        return Response(
            {"error": "Failed to create request."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# @pk - club join request id
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def approve_club_join_request(request, pk):
    user = request.user
    join_request = ClubJoinRequest.objects.get(pk=pk)

    if user.id != join_request.club.club_leader.id:
        return Response(
            {"error": "You don't have permissions to approve the request."},
            status=status.HTTP_403_FORBIDDEN,
        )

    join_request_user = User.objects.get(pk=join_request.user.id)

    join_request_user.club = join_request.club
    join_request_user.save()

    join_request.is_approved = True
    join_request.save()

    serializer = ClubJoinRequestSerializer(join_request)

    return Response(serializer.data)


# @pk - club id
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_club_members(request, pk):
    try:
        members = User.objects.all().filter(club=pk)

        serializer = UserSerializer(members, many=True)

        return Response({"count": len(members), "data": serializer.data})

    except:
        return Response(
            {"error": "Could not get club members."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
