import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import login
from .models import Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        Room.objects.create(room_name=self.channel_name)

        await login(self.scope, self.user)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        Room.objects.filter(room_name=self.channel_name).delete
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        utc_time = datetime.datetime.now(datetime.timezone.utc)
        utc_time = utc_time.isoformat()
        user = self.scope["user"]
        username = user.username
        message = (username + ': ' + message + ' : ' + utc_time)

        await login(self.scope, user)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'utc_time': utc_time,
                'username': username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        utc_time = event['utc_time']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'utc_time': utc_time,
            'username': username,
        }))
