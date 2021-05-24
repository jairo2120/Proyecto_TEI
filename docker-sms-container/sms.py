import clx.xms 
import requests
import json

def sendSms(numero,mensaje):
    client = clx.xms.Client(service_plan_id="f9f63dc704e54b949e3775ba11b7d890",token="0a6684af088d41f29d9e1d9bcd35e72f")
    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = numero
    create.recipients = {numero}
    create.body = mensaje

    try:
        batch = client.create_batch(create)
    except (requests.exceptions.RequestsException,clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))