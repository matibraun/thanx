from rest_framework import viewsets
from rest_framework.response import Response
from app.transaction.models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that handles listing and creating rewards
    """
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request):

        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        
        return Response(serializer.data)