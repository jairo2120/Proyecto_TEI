import clx.xms #proyecto123*
import requests 
import json  
def sms_adapter(phone,message):
    client = clx.xms.Client(service_plan_id=SERVICE_PLAN_ID,token=TOKEN) #SERVICE_PLAN_ID #TOKEN
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = phone
    create.recipients = {phone}
    create.body = message
    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestsException,clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))
    