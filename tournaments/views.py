from rest_framework import generics, permissions, status
from rest_framework.views import Response
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
)


class TournamentsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentSerializer


class TournamentDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TournamentJoinRequestList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TournamentJoinRequestSerializer


class TournamentJoinRequestDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = TournamentJoinRequest.objects.all()
    serializer_class = TournamentJoinRequestSerializer


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

    queryset = TournamentRoomTeam.objecst.all()

    serializer_class = TournamentRoomTeamSerializer
