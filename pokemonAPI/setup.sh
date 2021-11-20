#!/bin/bash
sudo apt-get update
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo python3 -m pip install --upgrade pip
sudo pip3 install flask
sudo apt-get install git -y 
git clone https://github.com/mdewinged/tac-nuvem.git
sudo (crontab -l 2>/dev/null; echo \"@reboot sudo python3 /home/testadmin/tac-nuvem/pokemonAPI/main.py\") | crontab -