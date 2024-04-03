from django.urls import path
from .views import (
    TournamentDetails,
    TournamentJoinRequestDetails,
    TournamentJoinRequestList,
    TournamentJudgesList,
    TournamentTeamDetails,
    TournamentTeamList,
    TournamentsList,
)

urlpatterns = [
    path("tournaments/", TournamentsList.as_view(), name="Tournaments list"),
    path(
        "tournaments/<int:pk>", TournamentDetails.as_view(), name="Tournament Details"
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
        name="Tournaemnt team details",
    ),
    path(
        "tournament-judges/",
        TournamentJudgesList.as_view(),
        name="Tournament judges list",
    ),
]
