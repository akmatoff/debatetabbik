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

app_name = "tournaments"

urlpatterns = [
    path("", TournamentsList.as_view(), name="Tournaments list"),
    path("<int:pk>", TournamentDetails.as_view(), name="Tournament Details"),
    path(
        "<int:tournament_id>/get_join_requests",
        get_tournamnet_join_requests,
        name="Tournament join requests list",
    ),
    path(
        "join-requests/",
        TournamentJoinRequestList.as_view(),
        name="Tournament join requests list",
    ),
    path(
        "join-requests/<int:pk>",
        TournamentJoinRequestDetails.as_view(),
        name="Tournament join request details",
    ),
    path("teams/", TournamentTeamList.as_view(), name="Tournament teams list"),
    path(
        "teams/<int:pk>",
        TournamentTeamDetails.as_view(),
        name="Tournament team details",
    ),
    path(
        "judges/",
        TournamentJudgesList.as_view(),
        name="Tournament judges list",
    ),
    path(
        "team-invitations/",
        UserTournamentTeamInvitationList.as_view(),
        name="User tournament team invitation list",
    ),
]
