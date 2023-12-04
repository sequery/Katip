from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from users.models import User
from foods.models import Food_Category, Food, Food_Size, Hall, Table
from users.api.serializers import UserSerializer


# Food Category Api View

class UserApiListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
