pushd ../
#npm run build
#cd dist
#zip -r evote-web.zip ./
#aws s3 cp evote-web.zip s3://alexbc.demoapp --region us-east-1 --acl public-read
#rm evote-web.zip


cp ../cast_vote/voto_registro.py .
docker build -t eleicoes .
rm voto_registro.py
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 771620814942.dkr.ecr.us-west-2.amazonaws.com
docker tag eleicoes:latest 771620814942.dkr.ecr.us-west-2.amazonaws.com/eleicoes:latest
docker push 771620814942.dkr.ecr.us-west-2.amazonaws.com/eleicoes:latest

#install in the cluster
kubectl create deployment eleicoes-app-ec2 --image=771620814942.dkr.ecr.us-west-2.amazonaws.com/eleicoes
kubectl expose deployment eleicoes-app-ec2 --type=LoadBalancer --port 5000 --target-port 5000


#docker run -p 5000:5000 eleicoes
