import json
from flask import Flask, render_template, json

import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

import sys
sys.path.insert(1, '../cast_vote')
from voto_registro import *

app = Flask(__name__,template_folder='.')

xray_recorder.configure(service='cast_vote_flask')
XRayMiddleware(app, xray_recorder)

@app.route("/")

def index():
    logging.basicConfig(level = logging.INFO)
    logging.info("** Aplicacao Iniciada **")

    eleitor=get_eleitor_code()
    put_voto(eleitor, "83")
    logging.info("** Eleitor:" + eleitor)
    data = '{ "eleitor":%s}' % (eleitor)

    return render_template('index.html', jsonfile=json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')