#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

sudo apt update -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

config="/etc/nginx/sites-available/default"
location=$(grep -Fn location $config | head -1 | cut -d":" -f1)
hbnb_static="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "${location}i ${hbnb_static}" "${config}"

sudo service nginx restart