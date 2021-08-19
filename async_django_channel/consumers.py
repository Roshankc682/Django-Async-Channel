from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TestConsumer(WebsocketConsumer):

    def connect(self, *args,**kwargs):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected to first channel '}))

    def receive(self,text_data):
        print(text_data)
        self.send(text_data=json.dumps({'message': 'first channel got message'}))
        pass

    def disconnect(self, *args,**kwargs):
        print("disconnected from first")
        # pass

    def send_notification(self,event):
        print("send notification to first channel")
        date = json.loads(event.get('value'))
        print(event)
        self.send(text_data=json.dumps(date))


class NewClass(AsyncJsonWebsocketConsumer):
    async def connect(self, *args,**kwargs):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected to new channel '}))

    async def receive(self,text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'message': 'new channel got message'}))
        # pass

    async def disconnect(self, *args,**kwargs):
        print("disconnected from first")
        # pass

    async def send_notification(self,event):
        date = json.loads(event.get('value'))
        print(event)
        await self.send(text_data=json.dumps(date))
