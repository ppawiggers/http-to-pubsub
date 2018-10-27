import os
import json

from google.cloud import pubsub

client = pubsub.PublisherClient()


def F(request):
    data = json.dumps({
        "headers": dict(request.headers),
        "body": request.get_json(),
    })
    client.publish(os.getenv('PUBSUB_TOPIC_PATH'), data.encode())

    return data
