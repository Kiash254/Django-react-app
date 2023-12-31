from django.urls import path
from .views import room_list, room_create, room_detail


app_name='api'
urlpatterns = [
    path('api/rooms/', room_list, name='room_list'),
    path('api/rooms/create/', room_create, name='room_create'),
    path('api/rooms/<int:pk>/', room_detail, name='room_detail'),
]