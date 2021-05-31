import clx.xms #proyecto123*
import requests 
import json  
import os

your_service_plan_id = os.getenv('SERVICE_PLAN_ID')
your_token = os.getenv('TOKEN') 
def sms_adapter(phone,message):
    client = clx.xms.Client(service_plan_id=your_service_plan_id,token=your_token) #SERVICE_PLAN_ID #TOKEN
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = phone
    create.recipients = {phone}
    create.body = message
    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestsException,clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))
    