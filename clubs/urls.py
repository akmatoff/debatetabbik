from django.urls import path
from .views import ClubsList, ClubDetails

urlpatterns = [
    path('clubs/', ClubsList.as_view(), name="Clubs list"),
    path('clubs/<int:pk>', ClubDetails.as_view(), name="Club details")
]