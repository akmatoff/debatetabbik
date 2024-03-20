from rest_framework import generics
from rest_framework import permissions
from .models import Club, ClubJoinRequest
from .serializers import ClubSerializer, ClubJoinRequestSerializer

class ClubsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubJoinRequestsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer

class ClubJoinRequestsDetails(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer