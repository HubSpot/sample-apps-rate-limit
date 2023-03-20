import os
import threading
import time
from http import HTTPStatus

from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.objects.exceptions import ApiException


def get_access_token():
    load_dotenv()
    return os.environ['ACCESS_TOKEN']


def call_api():
    api_client = HubSpot(access_token=get_access_token())
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            api_client.crm.objects.basic_api.get_page(object_type="contact")
            break  # Exit the loop if the API call succeeds
        except ApiException as e:
            if e.status == HTTPStatus.TOO_MANY_REQUESTS:
                print("Rate limit exceeded, retrying in 5 seconds...")
                time.sleep(5)
                retries += 1
            else:
                raise  # Reraise the exception if it's not a rate limit error


for _ in range(200):
    t = threading.Thread(target=call_api)
    t.start()
