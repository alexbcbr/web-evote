import json
import boto3
import logging
import os

from aws_xray_sdk.core import patch_all 
from voto_registro import *

patch_all()

trace_level = os.environ['TRACE_LEVEL']
sqs_queue_url = os.environ['SQS_QUEUE_URL']

def handler(event, context):

    logging.getLogger().setLevel(trace_level)
    #logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))

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
