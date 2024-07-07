from rest_framework import generics
from .models import Message, Room
from .serializers import MessageSerializer, RoomSerializer

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Message.objects.filter(room_id=room_id)
