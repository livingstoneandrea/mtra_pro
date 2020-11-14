from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationConsumer(WebsocketConsumer):
    
    # Function to connect to the websocket
    def connect(self):
       # Checking if the User is logged in
        if self.scope["user"].is_anonymous:
            print(self.scope["user"])
            # Reject the connection
            self.close()
        else:
            print(self.scope["user"])   # Can access logged in user details by using self.scope.user, Can only be used if AuthMiddlewareStack is used in the routing.py
            self.group_name = str(self.scope["user"].pk)  # Setting the group name as the pk of the user primary key as it is unique to each user. The group name is used to communicate with the user.
            print(f'group name {self.group_name}')
            async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
            self.accept()

    # Function to disconnet the Socket
    def disconnect(self, close_code):
        self.close()
        # pass

    # Custom Notify Function which can be called from Views or api to send message to the frontend
    def notify(self, event):
        self.send(text_data=json.dumps(event["text"])) 
        
class NoseyConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('user_notifier',self.channel_name)
        print(f'Added {self.channel_name} channel to New user gossip')
        pass
    async def disconnect(self):
        await self.channel_layer.group_discard('user_notifier',self.channel_name)
        print(f'Removed {self.channel_name} channel to New user gossip')
        pass
    
    async def new_userNotifier(self,event):
        await self.send_json(event)
        print(f'Got message {event} at {self.channel_name}')
    pass        