import json
import boto3
import logging
import os

from aws_xray_sdk.core import patch_all 
from voto_registro import *

patch_all()

sqs_queue_url = os.environ['SQS_QUEUE_URL']
#trace_level = os.environ['TRACE_LEVEL']

def handler(event, context):
    trace_level = get_trace_level()
    print("Trace Level" + trace_level)

    logging.getLogger().setLevel(trace_level)

    eleitor=get_eleitor_code()
    candidato=check_candidato_code(event['pathParameters']['num_candidato'])

    logging.info(candidato)
    put_voto(eleitor, candidato)
    send_message_voto(sqs_queue_url, candidato)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "eleitor": eleitor,
        }),
    }
