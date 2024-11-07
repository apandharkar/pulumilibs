import pulumi
import pulumi_aws as aws

class Vpc:

    def __init__(self, name, cidr):

        self.name = name

        self.vpc = aws.ec2.Vpc(
            self.name,
            cidr_block=cidr
        )