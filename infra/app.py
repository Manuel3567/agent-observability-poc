#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    Stack,
)
from constructs import Construct
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_iam as iam
from aws_cdk import aws_ec2 as ec2

from dotenv import load_dotenv


class AgentStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc.from_vpc_attributes(self, "VPC", availability_zones=["eu-central-1a", "eu-central-1b", "eu-central-1c"], vpc_id=vpc_id)
        cluster = ecs.Cluster(self, "Cluster", vpc=vpc)
        task_role = iam.Role(
            self, "MyRole", assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com")
        )
        task_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
        )
        task_definition = ecs.FargateTaskDefinition(
            self, "TaskDef", memory_limit_mib=512, cpu=256, task_role=task_role
        )

        task_definition.add_container(
            "DefaultContainer",
            image=ecs.ContainerImage.from_asset("../app/"),
        )


# Define your constructs here

load_dotenv()
app = cdk.App()
vpc_id = os.environ["VPC_ID"]

AgentStack(app, "AgentStack", vpc_id)

app.synth()
