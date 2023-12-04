from django.urls import path
from foods.views import *



app_name = 'foods'

urlpatterns = [
    # Create
    path('create/', CreateHomeView.as_view(), name='create'),
    path('foods/create/', AddFoodView.as_view(), name='add-food'),
    path('categories/create/', AddFoodCategoryView.as_view(), name='add-food_category'),
    path('food-sizes/create/', AddFoodSizeView.as_view(), name='add-food_size'),
    path('halls/create/', AddHallView.as_view(), name='add-hall'),
    path('tables/create/', AddTableView.as_view(), name='add-table'),
    path('orders/create/', AddOrderView.as_view(), name='add-order'),
    path('order-items/create/', AddOrderItemView.as_view(), name='add-order_item'),
    # List
    path('categories/', FoodCategoryListView.as_view(), name='food_category-list'),
    path('foods/', FoodListView.as_view(), name='food-list'),
    path('halls/', HallListView.as_view(), name='hall-list'),
    path('tables/', TableListView.as_view(), name='table-list'),
    path('orders/', OrdersListView.as_view(), name='order-list'),
    # Update
    path('categories/edit/<int:pk>', UpdateFoodCategoryView.as_view(), name='update-food_category'),
    path('foods/edit/<int:pk>', UpdateFoodView.as_view(), name='update-food'),
    path('food-sizes/edit/<int:pk>', UpdateFoodSizeView.as_view(), name='update-food_size'),
    path('halls/edit/<int:pk>', UpdateHallView.as_view(), name='update-hall'),
    path('tables/edit/<int:pk>', UpdateTableView.as_view(), name='update-table'),
    path('orders/edit/<int:pk>', UpdateOrderView.as_view(), name='update-order'),
    # Delete
    path('categories/delete/<int:pk>', DeleteFoodCategoryView.as_view(), name='delete-food_category'),
    path('food/delete/<int:pk>', DeleteFoodView.as_view(), name='delete-food'),
    path('food-size/delete/<int:pk>', DeleteFoodSizeView.as_view(), name='delete-food_size'),
    path('halls/delete/<int:pk>', DeleteHallView.as_view(), name='delete-hall'),
    path('tables/delete/<int:pk>', DeleteTableView.as_view(), name='delete-table'),
    path('orders/delete/<int:pk>', DeleteOrderView.as_view(), name='delete-order'),
    # Detail
    path('foods/<int:pk>', DetailFoodView.as_view(), name='detail-food'),
    path('categories/<int:pk>', DetailFoodCategoryView.as_view(), name='detail-food_category'),
    path('halls/<int:pk>', DetailHallView.as_view(), name='detail-hall'),
    path('tables/<int:pk>', DetailTableView.as_view(), name='detail-table'),
    path('orders/<int:pk>', DetailOrderView.as_view(), name='detail-order'),
    # Printer
]