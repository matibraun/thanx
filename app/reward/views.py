from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app.reward.models import Redemption, Reward
from app.user.models import User
from app.transaction.models import Transaction
from .serializers import RedemptionSerializer, RewardSerializer, RewardOutputSerializer


class RewardViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that handles listing and creating rewards
    """
    
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    def list(self, request):

        queryset = self.get_queryset()
        serializer = RewardOutputSerializer(queryset, many=True)
        
        return Response(serializer.data)

    def create(self, request):

        serializer = RewardSerializer(data=request.data)
        
        if serializer.is_valid():
            
            reward = Reward(
                name=serializer._validated_data["name"],
                description=serializer._validated_data["description"],
                points_required=serializer._validated_data["points_required"],
                available=serializer._validated_data["available"],
            )
            reward.full_clean()
            reward.save() 

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvailableRewardViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that handles listing available rewards
    """
    
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    def list(self, request):

        queryset = self.get_queryset().filter(available=True)
        serializer = RewardOutputSerializer(queryset, many=True)
        
        return Response(serializer.data)



class RedemptionViewSet(viewsets.ViewSet):
    """
    A ViewSet that handles listing and retrieving redemptions.
    """

    def list(self, request):

        queryset = Redemption.objects.all()
        serializer = RedemptionSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, user_id=None):

        queryset = Redemption.objects.filter(user_id=user_id)
        serializer = RedemptionSerializer(queryset, many=True)
        
        if not serializer.data:
            return Response({'detail': 'No redemptions found for this user.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)
    

    def create(self, request):

        reward_id = request.data.get('reward_id')
        user_id = request.data.get('user_id')

        reward = get_object_or_404(Reward, id=reward_id)
        user = get_object_or_404(User, id=user_id)

        transaction = Transaction(
            user=user,
            points=-reward.points_required,
            type_id=2
        )

        try:

            transaction.full_clean()
            transaction.save()
            
            redemption = Redemption(reward=reward, user=user)
            redemption.save()

            serializer = RedemptionSerializer(redemption)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:

            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)