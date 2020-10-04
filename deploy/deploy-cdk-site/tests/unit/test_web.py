import json
import pytest

from aws_cdk import core
from stack.web import DeployWebStack

def get_template():
    app = core.App()
    DeployWebStack(app, "deploy-cdk-evote-web")
    return json.dumps(app.synth().get_stack("deploy-cdk-evote-web").template)

def test_ec2_instance_created():
    assert("AWS::EC2::Instance" in get_template())

#def test_ecs_container_created():
#    assert("AWS::ECS::Cluster" in get_template())
