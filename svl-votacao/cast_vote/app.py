import json
import boto3
import logging
from aws_xray_sdk.core import patch_all 
from voto_registro import *

# import requests

patch_all()

def handler(event, context):

    logging.getLogger().setLevel(logging.ERROR)
    eleitor=get_eleitor_code()
    put_voto(eleitor, "90")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": eleitor,
        }),
    }
