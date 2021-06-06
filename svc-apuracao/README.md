##build container image locally
docker build -t apuracao_flask .
docker run -d -p 8080:80 --name apuracao apuracao_flask
curl http://localhost:8080

##debug
docker exec -it flask /bin/bash
docker run -it python-flask /bin/bash

##create ECR following the commands (copy and paste from console)
aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 771620814942.dkr.ecr.sa-east-1.amazonaws.com
docker tag apuracao_flask:latest 771620814942.dkr.ecr.sa-east-1.amazonaws.com/demo:latest
docker push 771620814942.dkr.ecr.sa-east-1.amazonaws.com/demo:latest

##create and cluster deployment
kubectl config get-contexts
eksctl create cluster --name el2 --region sa-east-1
kubectl create deployment apuracao-app --image=771620814942.dkr.ecr.sa-east-1.amazonaws.com/demo:latest
kubectl get deployment
kubectl expose deployment apuracao-app --type=LoadBalancer --port 8080 --target-port=8080
kubectl get nodes
kubectl get service

