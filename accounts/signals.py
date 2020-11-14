from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.datetime_safe import datetime


@receiver(post_save, sender=User)
def notify_new_user_signal(sender, instance, created, **kwargs):
    if created:
        current_user = instance # Getting current user
        channel_layer = get_channel_layer()
        data = "notification"+ ".New user "+instance.username+" has joined @ -." + str(datetime.now()) 
        
        print(f'user = {current_user} data {data}')
        # Trigger message sent to group
        async_to_sync(channel_layer.group_send)(
            "user_notifier",  # Group Name, Should always be string
            {
                "type": "new_userNotifier",   # Custom Function written in the consumers.py
                "event":"New User",
                "text": data,
            },
        )    
        
    
    
    
