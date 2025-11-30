#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    Stack,
)
from constructs import Construct


class HelloCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define your constructs here



app = cdk.App()
HelloCdkStack(
    app,
    "HelloCdkStack",
)

app.synth()
