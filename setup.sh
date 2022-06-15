#!/bin/bash

echo "Install python version 3.6"
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.6 python3.6-dev python3.6-venv -y

echo "Install gnu parallel"
sudo apt install parallel -y

echo "Install screen"
sudo apt-get install screen -y

echo "Initialize new screen"
screen -S rl-parallel

echo "Generate python virtual environment"
python3.6 -m venv venv1

echo "Activate virtual environment"
cd venv1 && source bin/activate

echo "Install dependency"
pip install -r requirements.txt

echo "Run training script"
source .script/run_parallel.sh

echo "Train and Test Agent completely!"
