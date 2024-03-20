from rest_framework import generics, permissions
from rest_framework.views import APIView, Response
from .models import User
from .serializers import UserSerializer

class UsersList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserData(APIView):
    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)