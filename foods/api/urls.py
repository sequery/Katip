from foods.views import HallListView
from django.urls import path
from foods.api.views import FoodCategoryApiListView, FoodCategoryApiDetailView, FoodApiListView, FoodApiDetailView, FoodSizeApiListView, FoodSizeApiDetailView, HallApiListView, HallApiDetailView, TableApiDetailView, TableApiListView



app_name = 'api'

urlpatterns = [
    path('food-categories/', FoodCategoryApiListView.as_view(), name='food-category-api'),
    path('food-categories/<int:pk>/', FoodCategoryApiDetailView.as_view(), name='food-category-detail-api'),
    path('food/', FoodApiListView.as_view(), name='food-api'),
    path('food/<int:pk>/', FoodApiDetailView.as_view(), name='food-detail-api'),
    path('food-sizes/', FoodSizeApiListView.as_view(), name='food-size-api'),
    path('food-sizes/<int:pk>/', FoodSizeApiDetailView.as_view(), name='food-size-detail-api'),
    path('halls/', HallApiListView.as_view(), name='hall-api'),
    path('halls/<int:pk>/', HallApiDetailView.as_view(), name='hall-detail-api'),
    path('tables/', TableApiListView.as_view(), name='table-api'),
    path('tables/<int:pk>/', TableApiDetailView.as_view(), name='table-detail-api'),
]