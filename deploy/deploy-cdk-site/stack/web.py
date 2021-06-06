import os.path
from aws_cdk.aws_elasticloadbalancingv2 import HealthCheck

from aws_cdk.aws_s3_assets import Asset
from aws_cdk.core import App, Duration, Tags

from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_elasticloadbalancing as elb,
    aws_autoscaling as autoscaling,
    core
)

dirname = os.path.dirname(__file__)

class DeployWebStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "VPC",
            nat_gateways=0,
            subnet_configuration=[ec2.SubnetConfiguration(name="public",subnet_type=ec2.SubnetType.PUBLIC)]
        )

        # Instance Role and SSM Managed Policy
        role = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))

        #security group
        electionSG = ec2.SecurityGroup(self, "EleicoesSecurityGroup",
            description= "Allow ssh access to ec2 instances",
            security_group_name= "EleicoesSecurityGroup",
            vpc= vpc,
            allow_all_outbound=True
        )
        electionSG.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "allow ssh access from the world")
        electionSG.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), "allow http access")

        # AMI 
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        # Script in S3 as Asset
        asset = Asset(self, "Asset", path=os.path.join(dirname, "configure.sh"))

        # Instance
        instance = ec2.Instance(self, "Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc = vpc,
            role = role,
            security_group = electionSG,
        )
        local_path = instance.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key
        )
        instance.user_data.add_execute_file_command(
            file_path=local_path
        )
        asset.grant_read(instance.role)

        # autoscaling group
        asg = autoscaling.AutoScalingGroup(
            self, "ASG",
            vpc=vpc,
            instance_type=ec2.InstanceType("t2.small"),
            role = role,
            security_group = electionSG,
            machine_image=amzn_linux
        )
        local_path_ASG = asg.user_data.add_s3_download_command(
            bucket=asset.bucket,
            bucket_key=asset.s3_object_key
        )
        Tags.of(asg).add("ambiente", "producao")
        Tags.of(asg).add("cliente", "tdc")
        asg.user_data.add_execute_file_command(
            file_path=local_path
        )
        asset.grant_read(asg.role)

        ### Load Balancer
        lb = elb.LoadBalancer(
            self, "LB",
            vpc=vpc,
            internet_facing=True,
            health_check=elb.HealthCheck(port=80, unhealthy_threshold=2, timeout=Duration.seconds(2), interval=Duration.seconds(5)),
        )

        lb.add_target(asg)
        listener = lb.add_listener(external_port=80)
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")
