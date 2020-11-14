from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.datetime_safe import datetime


current_user = request.user # Getting current user
channel_layer = get_channel_layer()
data = "notification"+ "...." + str(datetime.now()) # Pass any data based on your requirement
# Trigger message sent to group
async_to_sync(channel_layer.group_send)(
    str(current_user.pk),  # Group Name, Should always be string
    {
        "type": "notify",   # Custom Function written in the consumers.py
        "text": data,
    },
)