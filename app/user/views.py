from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app.transaction.models import Transaction
from app.user.models import User
from .serializers import UserSerializer
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
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):

        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            
            user = User(
                email=serializer._validated_data["email"],
                first_name=serializer._validated_data["first_name"],
                last_name=serializer._validated_data["last_name"],
                country_code=serializer._validated_data["country_code"],
                phone=serializer._validated_data["phone"],
                document_type=serializer._validated_data["document_type"],
                document_number=serializer._validated_data["document_number"],
                address=serializer._validated_data["address"],
                nationality=serializer._validated_data["nationality"],
                gender=serializer._validated_data["gender"],
                civil_state=serializer._validated_data["civil_state"],
            )
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

            return Response({'user_id': user.id, 'points_balance': total_points}, status=status.HTTP_200_OK)
        
        except User.DoesNotExist:

            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)