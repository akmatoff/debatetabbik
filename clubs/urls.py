from django.urls import path
from .views import (
    ClubsList,
    ClubDetails,
    ClubJoinRequestsList,
    ClubJoinRequestsDetails,
    approve_club_join_request,
    get_join_requests,
    join_club,
    request_to_join_club,
    get_club_members,
)

app_name = "clubs"

urlpatterns = [
    path("", ClubsList.as_view(), name="Clubs list"),
    path("<int:pk>", ClubDetails.as_view(), name="Club details"),
    path(
        "<int:pk>/request_to_join",
        request_to_join_club,
        name="Request to join the club",
    ),
    path("<int:pk>/get_members", get_club_members, name="Get club members"),
    path("<int:pk>/join_club", join_club, name="Join club"),
    path(
        "<int:pk>/get_join_requests",
        get_join_requests,
        name="Club join requests",
    ),
    path("join-requests/", ClubJoinRequestsList.as_view(), name="Club join requests"),
    path(
        "join-requests/<int:pk>",
        ClubJoinRequestsDetails.as_view(),
        name="Club join request details",
    ),
    path(
        "join-requests/<int:pk>/approve_request",
        approve_club_join_request,
        name="Approve club join request",
    ),
]
