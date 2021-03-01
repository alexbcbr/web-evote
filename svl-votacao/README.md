# svl-votacao
# SVL - Service based on Lambda
# SVC - Service based on container
# SVS - Service based on server (EC2)

```bash
sam build
sam deploy --guided

curl https://wmq21dm5gb.execute-api.us-east-1.amazonaws.com/Prod/vote
sam logs -n VotarFunction --stack-name svl-votacao --tail

aws cloudformation delete-stack --stack-name svl-votacao

```

Running SVL-votacao in Flash
pip install aws-xray-sdk

Download XRay local daemon
https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html

How to use X-Ray local daemon
https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-local.html