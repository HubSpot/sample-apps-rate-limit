import os
import threading

from dotenv import load_dotenv
from hubspot import HubSpot


def get_access_token():
    load_dotenv()
    return os.environ['ACCESS_TOKEN']


def call_api():
    api_client = HubSpot(access_token=get_access_token())
    api_client.crm.objects.basic_api.get_page(object_type='contact')


for _ in range(1000):
    try:
        thread = threading.Thread(target=call_api)
        thread.start()
    except Exception as e:
        print(e)
