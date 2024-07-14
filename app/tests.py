
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Room, Message

class RoomAPITests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.create_user(username='user', password='user')
        self.room = Room.objects.create(name='Test Room')

    def test_create_room(self):
        self.client.login(username='admin', password='admin')
        url = reverse('room-list-create')
        data = {'name': 'New Room', 'description': 'New Room Description'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_rooms(self):
        url = reverse('room-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class MessageAPITests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.create_user(username='user', password='user')
        self.room = Room.objects.create(name='Test Room')

    def test_create_message(self):
        self.client.login(username='user', password='user')
        url = reverse('message-list-create', args=[self.room.id])
        data = {'content': 'Test message', 'room': self.room.id}
        response = self.client.post(url, data, format='json')
        print("Response Content:", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_messages(self):
        Message.objects.create(user=self.user, room=self.room, content='Test message')
        url = reverse('message-list-create', args=[self.room.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
