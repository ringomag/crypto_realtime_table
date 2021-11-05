from channels.generic.websocket import AsyncWebsocketConsumer
import json

class WSCoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "coin"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def socket_get_coins(self, event):
        message = event['text']
        await self.send(json.dumps(message))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)