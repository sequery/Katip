from foods.views import HallListView
from django.urls import path
from users.api.views import UserApiDetailView, UserApiListView



app_name = 'api'

urlpatterns = [
    path('users/', UserApiListView.as_view(), name='users-api'),
    path('users/<int:pk>/', UserApiDetailView.as_view(), name='users-detail-api'),
]