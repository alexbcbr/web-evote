#pushd ../
docker build -t eleicoes .
docker tag demo:latest 771620814942.dkr.ecr.us-west-2.amazonaws.com/eleicoes:latest
docker push 771620814942.dkr.ecr.us-west-2.amazonaws.com/eleicoes:latest

#npm run build
#cd dist
#zip -r evote-web.zip ./
#aws s3 cp evote-web.zip s3://alexbc.demoapp --region us-east-1 --acl public-read
#rm evote-web.zip

