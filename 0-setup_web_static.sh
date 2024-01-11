#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

sudo apt update -y
sudo apt install nginx -y

sudo mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"
sudo chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart