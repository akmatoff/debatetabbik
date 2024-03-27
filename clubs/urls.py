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

urlpatterns = [
    path("clubs/", ClubsList.as_view(), name="Clubs list"),
    path("clubs/<int:pk>", ClubDetails.as_view(), name="Club details"),
    path(
        "clubs/<int:pk>/request_to_join",
        request_to_join_club,
        name="Request to join the club",
    ),
    path("clubs/<int:pk>/get_members", get_club_members, name="Get club members"),
    path("clubs/<int:pk>/join_club", join_club, name="Join club"),
    path(
        "clubs/<int:pk>/get_join_requests",
        get_join_requests,
        name="Club join requests",
    ),
    path(
        "club-join-requests/", ClubJoinRequestsList.as_view(), name="Club join requests"
    ),
    path(
        "club-join-requests/<int:pk>",
        ClubJoinRequestsDetails.as_view(),
        name="Club join request details",
    ),
    path(
        "club-join-requests/<int:pk>/approve_request",
        approve_club_join_request,
        name="Approve club join request",
    ),
]
