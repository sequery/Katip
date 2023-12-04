from rest_framework import serializers

from foods.models import Food, Food_Category, Food_Size, Hall, Table, Order, Order_Items


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Category
        fields = ['title', 'description', 'image', 'drink_category', 'parent_category', 'created', 'updated']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'description', 'image', 'category', 'discount', 'discount_unit', 'is_active', 'created', 'updated']

class FoodSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Size
        fields = ['title', 'food', 'price', 'created', 'updated']

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ['title', 'is_active', 'created', 'updated']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['number', 'hall', 'status', 'reserve_time', 'is_active', 'created', 'updated']