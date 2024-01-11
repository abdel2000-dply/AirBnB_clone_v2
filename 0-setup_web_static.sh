#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

apt update -y
apt install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart