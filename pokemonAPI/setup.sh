#! /bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3.8
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip
sudo pip install flask
sudo apt-get install git
git clone https://github.com/mdewinged/tac-nuvem.git
cd tac-nuvem/pokemonAPI/setup.sh
sudo python tac-nuvem/pokemonAPI/main.py
