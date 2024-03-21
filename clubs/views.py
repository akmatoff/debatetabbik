from rest_framework import generics, permissions, status
from rest_framework.views import Response
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

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if instance.club_leader_id == user.id:
            return super().delete(request, *args, **kwargs)
        
        return Response({ "message": "No permission to delete." }, status=status.HTTP_403_FORBIDDEN)

class ClubJoinRequestsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer

class ClubJoinRequestsDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = ClubJoinRequest.objects.all()
    serializer_class = ClubJoinRequestSerializer