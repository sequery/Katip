from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from users.models import User
from foods.models import Food_Category, Food, Food_Size, Hall, Table
from foods.api.serializers import FoodCategorySerializer, FoodSerializer, FoodSizeSerializer, HallSerializer, TableSerializer


# Food Category Api View

class FoodCategoryApiListView(ListCreateAPIView):
    queryset = Food_Category.objects.all()
    serializer_class = FoodCategorySerializer

class FoodCategoryApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Food_Category.objects.all()
    serializer_class = FoodCategorySerializer


# Food Api View

class FoodApiListView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


# Food Size Api View

class FoodSizeApiListView(ListCreateAPIView):
    queryset = Food_Size.objects.all()
    serializer_class = FoodSizeSerializer

class FoodSizeApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Food_Size.objects.all()
    serializer_class = FoodSizeSerializer


# Hall Api View

class HallApiListView(ListCreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class HallApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


# Table Api View

class TableApiListView(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableApiDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer