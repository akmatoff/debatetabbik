from rest_framework import generics, permissions, status
from rest_framework.views import Response
from rest_framework.decorators import api_view

from tabber_api.utils import parse_bool_query_param
from .serializers import (
    TournamentJudgePointSerializer,
    TournamentJudgeSerializer,
    TournamentRoomSerializer,
    TournamentRoomTeamSerializer,
    TournamentRoundPointSerializer,
    TournamentRoundSerializer,
    TournamentSerializer,
    TournamentJoinRequestSerializer,
    TournamentTeamSerializer,
    TournamentUserSpeakerPointSerializer,
    UserTournamentTeamInvitationSerializer,
)
from .models import (
    Tournament,
    TournamentJoinRequest,
    TournamentJudge,
    TournamentJudgePoint,
    TournamentRoom,
    TournamentRoomTeam,
    TournamentRound,
    TournamentRoundPoint,
    TournamentTeam,
    TournamentUserSpeakerPoint,
    UserTournamentTeamInvitation,
)


class TournamentsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentSerializer

    def get_queryset(self):
        queryset = Tournament.objects.all()

        is_approved = parse_bool_query_param(
            self.request.query_params.get("is_approved")
        )
        all_tournaments = parse_bool_query_param(
            self.request.query_params.get("all_tournaments")
        )

        queryset = queryset.filter(is_approved=True)

        if is_approved is not None:
            queryset = Tournament.objects.all().filter(is_approved=is_approved)

        if all_tournaments:
            queryset = Tournament.objects.all()

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TournamentDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentJoinRequestList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentJoinRequest.objects.all()
    serializer_class = TournamentJoinRequestSerializer


class TournamentJoinRequestDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentJoinRequest.objects.all()
    serializer_class = TournamentJoinRequestSerializer


@api_view(["GET"])
def get_tournamnet_join_requests(request, tournament_id):

    queryset = TournamentJoinRequest.objects.all().filter(tournament_id=tournament_id)
    serializer = TournamentSerializer(queryset, many=True)

    return Response(serializer.data)


class TournamentTeamList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentTeamSerializer


class TournamentTeamDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentTeam.objects.all()
    serializer_class = TournamentTeamSerializer


class TournamentJudgesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentJudgeSerializer


class TournamentJudgeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentJudge.objects.all()
    serializer_class = TournamentJudgeSerializer


class TournamentUserSpeakerPointsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentUserSpeakerPointSerializer


class TournamentUserSpeakerPointDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentUserSpeakerPoint.objects.all()
    serializer_class = TournamentUserSpeakerPointSerializer


class TournamentJudgePointsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentJudgePointSerializer


class TournamentJudgePointDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentJudgePoint.objects.all()
    serializer_class = TournamentJudgePointSerializer


class TournamentRoundsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentRoundSerializer


class TournamentRoundDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentRound.objects.all()
    serializer_class = TournamentRoundSerializer


class TournamentRoundPointsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentRoundPointSerializer


class TournamentRoundPointDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentRoundPoint
    serializer_class = TournamentRoundPointSerializer


class TournamentRoomsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentRoomSerializer


class TournamentRoomDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentRoom.objects.all()
    serializer_class = TournamentRoomSerializer


class TournamentRoomTeamsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentRoomTeamSerializer


class TournamentRoomTeamDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentRoomTeam.objects.all()

    serializer_class = TournamentRoomTeamSerializer


class UserTournamentTeamInvitationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = UserTournamentTeamInvitation.objects.all()

    serializer_class = UserTournamentTeamInvitationSerializer


class UserTournamentTeamInvitationDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = UserTournamentTeamInvitation.objects.all()

    serializer_class = UserTournamentTeamInvitationSerializer
