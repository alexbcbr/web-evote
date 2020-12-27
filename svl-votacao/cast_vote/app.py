import json
import boto3
from aws_xray_sdk.core import patch_all 

# import requests

patch_all()

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "vote",
            # "location": ip.text.replace("\n", "")
        }),
    }
