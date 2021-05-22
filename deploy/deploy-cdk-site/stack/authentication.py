from aws_cdk import (
    aws_iam as iam,
    #aws_cognito as cognito,
    core
)


class DeployAuthenticationStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cog = cognito.UserPool(
            self, "myuserpool",
            user_pool_name="myuserpool"
        )

