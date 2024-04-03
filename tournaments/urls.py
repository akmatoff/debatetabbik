from django.urls import path
from .views import (
    TournamentDetails,
    TournamentJoinRequestDetails,
    TournamentJoinRequestList,
    TournamentJudgesList,
    TournamentTeamDetails,
    TournamentTeamList,
    TournamentsList,
    UserTournamentTeamInvitationList,
    get_tournamnet_join_requests,
)

urlpatterns = [
    path("tournaments/", TournamentsList.as_view(), name="Tournaments list"),
    path(
        "tournaments/<int:pk>", TournamentDetails.as_view(), name="Tournament Details"
    ),
    path(
        "tournaments/<int:tournament_id>/get_join_requests",
        get_tournamnet_join_requests,
        name="Tournament join requests list",
    ),
    path(
        "tournament-join-requests/",
        TournamentJoinRequestList.as_view(),
        name="Tournament join requests list",
    ),
    path(
        "tournament-join-requests/<int:pk>",
        TournamentJoinRequestDetails.as_view(),
        name="Tournament join request details",
    ),
    path(
        "tournament-teams/", TournamentTeamList.as_view(), name="Tournament teams list"
    ),
    path(
        "tournament-teams/<int:pk>",
        TournamentTeamDetails.as_view(),
        name="Tournament team details",
    ),
    path(
        "tournament-judges/",
        TournamentJudgesList.as_view(),
        name="Tournament judges list",
    ),
    path(
        "tournament-team-invitations/",
        UserTournamentTeamInvitationList.as_view(),
        name="User tournament team invitation list",
    ),
]
