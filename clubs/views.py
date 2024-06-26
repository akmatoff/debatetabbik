from rest_framework import generics, permissions, status
from rest_framework.views import Response
from rest_framework.decorators import api_view, permission_classes
from drf_spectacular.utils import extend_schema
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

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context["user"] = self.request.user

        return context

    def create(self, request, *args, **kwargs):
        if request.user.club is not None:
            return Response(
                {"error": "You are already a member of a club"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        club = serializer.save(club_leader=self.request.user)

        self.request.user.club = club
        self.request.user.save()


class ClubDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context["user"] = self.request.user

        return context

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

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context["user"] = self.request.user

        return context


class ClubJoinRequestsDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context["user"] = self.request.user

        return context


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
        return Response(
            {"error": "Failed to create request."},
            status=status.HTTP_400_BAD_REQUEST,
        )


# @pk - club join request id
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def approve_club_join_request(request, pk):
    user = request.user

    try:
        join_request = ClubJoinRequest.objects.get(pk=pk)
    except:
        return Response({"error": "Could not find join request"})

    if user.id != join_request.club.club_leader.id:
        return Response(
            {"error": "You don't have permissions to approve the request."},
            status=status.HTTP_403_FORBIDDEN,
        )

    join_request.is_approved = True
    join_request.save()

    serializer = ClubJoinRequestSerializer(join_request)

    return Response(serializer.data)


# @pk - club id
@extend_schema(
    responses={200: UserSerializer(many=True)}, description="Get list of club members"
)
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
            status=status.HTTP_400_BAD_REQUEST,
        )


# @pk - club id
@extend_schema(
    responses={200: ClubJoinRequestSerializer(many=True)},
    description="Club join request list",
)
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_join_requests(request, pk):
    try:
        join_requests = ClubJoinRequest.objects.all().filter(club=pk)
    except:
        return Response(
            {"message": "No join requests found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = ClubJoinRequestSerializer(
        join_requests, many=True, context={"user": request.user}
    )

    return Response(serializer.data)


# @pk - club id
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def join_club(request, pk):
    user = request.user

    join_request = ClubJoinRequest.objects.get(user=user.id, club=pk)

    if join_request is None:
        return Response(
            {"error": "Join request not found"}, status=status.HTTP_400_BAD_REQUEST
        )

    if join_request.is_approved:
        join_request_user = User.objects.get(pk=user.id)

        join_request_user.club = join_request.club
        join_request_user.save()

        return Response({"message": "Join request approved successfully"})
    else:
        return Response(
            {"error": "Join request is not approved."},
            status=status.HTTP_400_BAD_REQUEST,
        )
