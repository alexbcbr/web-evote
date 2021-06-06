aws s3 cp s3://alexbc.demoapp/evote-web.zip .
docker build -t evote-web:beta . 
rm evote-web.zip
#docker run --name web -p 8080:80 -it evote-web:beta /bin/bash
docker run -d -p 8080:80 --name evote-web evote-web:beta


#docker start web

#curl http://localhost:8080