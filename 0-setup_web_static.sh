#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

if ! command -v nginx &> /dev/null
then
    sudo apt update
    sudo apt install nginx -y
    sudo service nginx start
fi

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

config="/etc/nginx/sites-available/default"
location=$(grep -Fn location $config | head -1 | cut -d":" -f1)
hbnb_static="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "${location}i ${hbnb_static}" "${config}"

sudo service nginx restart