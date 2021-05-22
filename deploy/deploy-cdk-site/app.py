#!/usr/bin/env python3

from aws_cdk import core

from stack.midleware import DeployMidlewareStack
from stack.web import DeployWebStack
from stack.authentication import DeployAuthenticationStack

app = core.App()
DeployMidlewareStack(app, "deploy-cdk-evote-midleware", env={'region': 'sa-east-1'})
DeployWebStack(app, "deploy-cdk-evote-web", env={'region': 'sa-east-1'})
#DeployAuthenticationStack(app, "deploy-cdk-evote-auth", env={'region': 'us-east-1'})

app.synth()
