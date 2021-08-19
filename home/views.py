from django.shortcuts import render
import time
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from faker import Faker
fake = Faker()
def home(request):
    channel_layer = get_channel_layer()
    for i in range(1,5):
        data = {"name":fake.name(),}
        async_to_sync(channel_layer.group_send)(
            'new_consumer_group',{
                # type is the function called from consumers
                'type':'send_notification',
                # this is the value send to send_notification function in consumer
                'value': json.dumps(data)
            }
        )
        # time.sleep(1)
    return render(request,'index.html')