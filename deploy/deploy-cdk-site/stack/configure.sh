#!/bin/sh
yum install -y httpd
systemctl start httpd
echo "Eleicoes 2020" > /var/www/html/index1.html
wget https://s3.amazonaws.com/alexbc.demoapp/evote-web.zip -P /var/www/html/
cd /var/www/html
unzip evote-web.zip
rm evote-web.zip