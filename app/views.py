from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.conf import settings
from django.http import JsonResponse
import pyaudio
import wave
import os
from .models import Message, Room
from .serializers import MessageSerializer, RoomSerializer
from .permissions import IsAdminOrReadOnly


class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Message.objects.filter(room_id=room_id)

