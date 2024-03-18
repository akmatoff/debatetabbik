from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        # user = User.objects.get(username=request.data['username'])

    return Response({})