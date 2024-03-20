from django.urls import path
from .views import ClubsList, ClubDetails, ClubJoinRequestsList, ClubJoinRequestsDetails

urlpatterns = [
    path('clubs/', ClubsList.as_view(), name="Clubs list"),
    path('clubs/<int:pk>', ClubDetails.as_view(), name="Club details"),
    path('club-join-requests/', ClubJoinRequestsList.as_view(), name="Club join requests"),
    path('club-join-requests/<int:pk>', ClubDetails.as_view(), name="Club join request details")
]