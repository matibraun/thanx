from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from app.transaction.models import Transaction
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db import models

class UserViewSet(viewsets.ViewSet):

    """
    A ViewSet that manually handles listing and creating users
    """

    def list(self, request):


        queryset = [
            {
                "email": "user0@example.com",
                "first_name": "First0",
                "last_name": "Last0",
                "country_code": "+1",
                "phone": "1234567890",
                "document_type": "ID Card",
                "document_number": "DOC1234",
                "address": "123 Random St, Cityville, Country",
                "nationality": "American",
                "gender": "male",
                "civil_state": "single"
            },
            {
                "email": "user1@example.com",
                "first_name": "First1",
                "last_name": "Last1",
                "country_code": "+44",
                "phone": "9876543210",
                "document_type": "Passport",
                "document_number": "DOC5678",
                "address": "456 Random St, Townsville, Country",
                "nationality": "British",
                "gender": "female",
                "civil_state": "married"
            },
            {
                "email": "user2@example.com",
                "first_name": "First2",
                "last_name": "Last2",
                "country_code": "+91",
                "phone": "5556781234",
                "document_type": "ID Card",
                "document_number": "DOC9012",
                "address": "789 Random St, Villagetown, Country",
                "nationality": "Indian",
                "gender": "other",
                "civil_state": "divorced"
            },
            {
                "email": "user3@example.com",
                "first_name": "First3",
                "last_name": "Last3",
                "country_code": "+49",
                "phone": "1237894560",
                "document_type": "Passport",
                "document_number": "DOC3456",
                "address": "321 Random St, Cityburg, Country",
                "nationality": "German",
                "gender": "male",
                "civil_state": "single"
            },
            {
                "email": "user4@example.com",
                "first_name": "First4",
                "last_name": "Last4",
                "country_code": "+34",
                "phone": "4561237890",
                "document_type": "ID Card",
                "document_number": "DOC7890",
                "address": "654 Random St, Metropolis, Country",
                "nationality": "Spanish",
                "gender": "female",
                "civil_state": "married"
            },
            {
                "email": "user5@example.com",
                "first_name": "First5",
                "last_name": "Last5",
                "country_code": "+81",
                "phone": "3214569870",
                "document_type": "Passport",
                "document_number": "DOC1235",
                "address": "987 Random St, Capital City, Country",
                "nationality": "Japanese",
                "gender": "other",
                "civil_state": "single"
            },
            {
                "email": "user6@example.com",
                "first_name": "First6",
                "last_name": "Last6",
                "country_code": "+61",
                "phone": "6547893210",
                "document_type": "ID Card",
                "document_number": "DOC5679",
                "address": "159 Random St, State Town, Country",
                "nationality": "Australian",
                "gender": "male",
                "civil_state": "divorced"
            },
            {
                "email": "user7@example.com",
                "first_name": "First7",
                "last_name": "Last7",
                "country_code": "+86",
                "phone": "7539518520",
                "document_type": "Passport",
                "document_number": "DOC9013",
                "address": "753 Random St, Province City, Country",
                "nationality": "Chinese",
                "gender": "female",
                "civil_state": "married"
            },
            {
                "email": "user8@example.com",
                "first_name": "First8",
                "last_name": "Last8",
                "country_code": "+1",
                "phone": "8529637410",
                "document_type": "ID Card",
                "document_number": "DOC3457",
                "address": "369 Random St, Region Town, Country",
                "nationality": "Canadian",
                "gender": "other",
                "civil_state": "single"
            },
            {
                "email": "user9@example.com",
                "first_name": "First9",
                "last_name": "Last9",
                "country_code": "+33",
                "phone": "2581473690",
                "document_type": "Passport",
                "document_number": "DOC7891",
                "address": "147 Random St, Country Town, Country",
                "nationality": "French",
                "gender": "male",
                "civil_state": "divorced"
            }
        ]


        # queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


class UserPointsBalanceView(APIView):
    """
    Retrieve the total points balance for a user.
    """

    def get(self, request, user_id):

        # user = get_object_or_404(User, id=user_id)
        # total_points = Transaction.objects.filter(user=user).aggregate(total=models.Sum('points'))['total'] or 0
        return Response({'user_id': user_id, 'points_balance': 100}, status=status.HTTP_200_OK)