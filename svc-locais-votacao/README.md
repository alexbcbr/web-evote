# Build container image locally

docker build -t flask_json:latest .
docker run -p 5000:5000 flask_json
curl http://0.0.0.0:5000/






docker run -d -p 8080:80 --name flask python-flask
curl http://localhost:8080

#debug
docker exec -it flask /bin/bash
docker run -it python-flask /bin/bash

#create ECR following the commands (copy and paste from console)
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 771620814942.dkr.ecr.us-east-1.amazonaws.com
docker build -t python-flask .
docker tag python-flask:latest 771620814942.dkr.ecr.us-east-1.amazonaws.com/python-flask:latest
docker push 771620814942.dkr.ecr.us-east-1.amazonaws.com/python-flask:latest

