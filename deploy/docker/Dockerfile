# Indicar a imagem base
#FROM ubuntu:18.04
FROM nginx:stable-alpine as production-stage

LABEL Alex BC

ENV VARIABLE1=development
ENV PORT=80

#append no arquivo para inicializar o apache de forma automatica
#RUN apt-get update
#RUN apt-get install -y apache2 apache2-utils curl unzip

#RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Criar um arquivo
COPY evote-web.zip /usr/share/nginx/html
#COPY evote-web.zip /var/www/html
WORKDIR /usr/share/nginx/html
RUN unzip -o evote-web.zip

EXPOSE $PORT
#RUN echo "service apache2 start" >> /etc/bash.bashrc 
#ENTRYPOINT ["apachectl", "-D", "FOREGROUND"]
CMD ["nginx", "-g", "daemon off;"]
