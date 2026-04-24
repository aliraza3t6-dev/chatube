import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import GlobalMessage
from asgiref.sync import sync_to_async

class GlobalChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = "global_chat"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        user = self.scope["user"]
        if not user.is_authenticated:
            return

        data = json.loads(text_data)
        message = data["message"]

        await sync_to_async(GlobalMessage.objects.create)(
            user=user,
            message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": user.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "user": event["user"],
        }))
