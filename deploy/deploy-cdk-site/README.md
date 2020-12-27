
# Welcome to eVote Demo using CDK

install constructs
python -m pip install aws-cdk.aws-s3 aws-cdk.aws-lambda aws-cdk.aws-cognito aws-cdk.aws-sns aws-cdk.aws-sns-subscription
https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html

At this point you can now synthesize the CloudFormation template for this code.

```bash
cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```bash
pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `cdk bootstrap`   bootstrap cdk for the first time in the region
* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation
* `cdk destroy`     destroy environment
* `cdk deploy "*"`  deploy all stacks (only valid with multiple stacks)
