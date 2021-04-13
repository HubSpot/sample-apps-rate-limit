import os
import threading
from dotenv import load_dotenv
from hubspot import HubSpot

def api_key():
  load_dotenv()
  return os.environ['HUBSPOT_API_KEY']

def call_api():
  api_client = HubSpot(api_key=api_key())
  api_client.crm.objects.basic_api.get_page(object_type='contact')

for _ in range(1000):
  try:
    thread = threading.Thread(target=call_api)
    thread.start()
  except hubspot.crm.objects.exceptions.ApiException as e:
    print(e)
