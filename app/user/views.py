from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app.transaction.models import Transaction
from app.user.models import User
from .serializers import UserSerializer, UserOutputSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import models

class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that handles listing and creating users
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserOutputSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = User(**serializer.validated_data)
            user.full_clean()
            user.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPointsBalanceView(APIView):
    """
    Retrieve the total points balance for a user.
    """

    def get(self, request, user_id):

        try:

            user = get_object_or_404(User, pk=user_id)

            total_points = Transaction.objects.filter(user_id=user_id).aggregate(total=models.Sum('points'))['total'] or 0

            return Response(
                {
                    'user_id': user.id,
                    'user_email': user.email,
                    'user_first_name': user.first_name,
                    'user_last_name': user.last_name,
                    'points_balance': total_points
                },
                status=status.HTTP_200_OK
            )
        
        except User.DoesNotExist:

            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)