# Indicar a imagem base
FROM ubuntu

LABEL Alex BC

ENV VARIABLE1=development
ENV PORT=80

#append no arquivo para inicializar o apache de forma automatica
RUN apt-get update && apt-get install -y apache2 curl unzip
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

#CMD "service apache2 start" >> /etc/bash.bashrc 
CMD ["service", "apache2", "start"]

# Criar um arquivo
COPY evote-web.zip /var/www/html
WORKDIR /var/www/html
RUN unzip -o evote-web.zip
#VOLUME ["/var/www"]

EXPOSE $PORT

#ENTRYPOINT ["node", "server.js"]
