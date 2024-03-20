from rest_framework import generics
from rest_framework import permissions
from .models import Club
from .serializers import ClubSerializer

class ClubsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Club.objects.all()
    serializer_class = ClubSerializer