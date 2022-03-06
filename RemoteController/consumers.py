import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
channel_layer = get_channel_layer()

import pyrebase
from .firebase_credentials import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

class HomeConsumer(AsyncWebsocketConsumer):
    device_group_name = "ESP32"
    async def connect(self):
        await self.channel_layer.group_add(
            self.device_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.device_group_name,
            self.channel_name
        )
    
    # Receive message from WebSocket
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        device_id = text_data_json['device_id']
        device_value = text_data_json['device_value']

        await self.channel_layer.group_send(
            self.device_group_name,
            {
                "type":"home.message",
                "message":{
                    'device_id':device_id,
                    'device_value':device_value
                }
            }
        )
        db.child("user").child(device_id).update({"status":device_value})
    
    async def home_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
def stream_handler(message):
    if len(message["path"]) > 1:
        if message["path"][3:] == "status":
            device_id = message["path"][1]
            device_value = message["data"]
            async_to_sync(channel_layer.group_send)(
                "ESP32",
                {
                    "type":"home.message",
                    "message":{
                        'device_id':device_id,
                        'device_value':device_value
                    }
                }
            )
        
db.child("user").stream(stream_handler)
        