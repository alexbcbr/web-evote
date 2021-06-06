import os
import boto3

session = boto3.Session()
ssm = session.client('ssm')

trace = ssm.get_parameter(Name="tracelevel", WithDecryption=False)
trace_txt = trace['Parameter']['Value']
print(type(str(trace_txt)))
print("trace: {}".format(trace['Parameter']['Value']))
