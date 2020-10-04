#!/usr/bin/env python3

from aws_cdk import core

from stack.midleware import DeployMidlewareStack
from stack.web import DeployWebStack


app = core.App()
DeployMidlewareStack(app, "deploy-cdk-evote-midleware", env={'region': 'sa-east-1'})
DeployWebStack(app, "deploy-cdk-evote-web", env={'region': 'sa-east-1'})

app.synth()
