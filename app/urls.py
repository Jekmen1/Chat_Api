from django.urls import path
from .views import RoomListCreate, MessageListCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:room_id>/messages/', MessageListCreate.as_view(), name='message-list-create'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
