#!/usr/bin/env bash
# Script to set up web server for deployment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

default_sites="/etc/nginx/sites-available/default"
location=$(grep -Fn location $default_sites | head -1 | cut -d":" -f1)
hbnb_static="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -hR ubuntu:ubuntu "/data/"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

echo "<html><head></head><body>Hello World!</body></html>" | sudo tee "/data/web_static/releases/test/index.html"


sudo sed -i "${location}i ${hbnb_static}" "${default_sites}"
sudo service nginx restart