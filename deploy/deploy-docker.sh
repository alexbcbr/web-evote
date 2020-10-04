pushd ../web
npm run build
cd dist
zip -r evote-web.zip ./
cp evote-web.zip ../../deploy

cd ../../deploy
#docker build -t evote-web:beta . 
#rm evote-web.zip
#docker run --name web -p 8080:80 -it evote-web:beta /bin/bash
#docker run --name web -p 8080:80 evote-web:beta
#docker start web

#curl http://localhost:8080