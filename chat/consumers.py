import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from message.models import Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'messages': 'You are now connected!'
        }))

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        color = text_data_json['color']

        mess = Message()
        mess.username = username
        mess.message = message
        mess.color = color
        mess.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
                'color': color,
            }
        )

        # print('Message: ', message)

        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        color = event['color']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'username': username,
            'color': color,
        }))