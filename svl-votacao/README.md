# svl-votacao

```bash
sam build
sam deploy --guided

curl https://wmq21dm5gb.execute-api.us-east-1.amazonaws.com/Prod/vote
sam logs -n VotarFunction --stack-name svl-votacao --tail

aws cloudformation delete-stack --stack-name svl-votacao

```