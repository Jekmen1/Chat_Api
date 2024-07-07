from django.urls import path
from .views import RoomListCreate, MessageListCreate

urlpatterns = [
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:room_id>/messages/', MessageListCreate.as_view(), name='message-list-create'),
]
