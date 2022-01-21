#!/bin/bash
g="\033[0;90m"
r="\033[0;91m"
terminator
clear
echo -e '\e[96m starting testnet...'
echo -e '\e[0m' 
sleep 1
xdotool type 'cd testnet/'
xdotool key KP_Enter
echo -e '\e[96m building & deploying test net...'
echo -e '\e[0m'
xdotool type './manage build --logs' #build von-network
xdotool key KP_Enter
sleep 11 
xdotool type './manage start --logs' #start von-network
xdotool key KP_Enter
echo -e '\e[34m done'
echo -e '\e[0m' 
echo -e '\e[96m starting webhook controller...'
echo -e '\e[0m' 
xdotool key shift+ctrl+E
sleep 1
xdotool type 'cd ..'
xdotool key KP_Enter
sleep 1
xdotool type 'docker-compose -f docker-compose-webhook.yml up --build' #start regov-controller
xdotool key KP_Enter
echo -e '\e[34m done'
echo -e '\e[0m' 
sleep 1
xdotool key shift+ctrl+O
clear
echo -e '\e[96m waiting for von-network to finish re-sync...'
echo -e '\e[0m' 
sleep 2
clear
echo -e '\e[0;33m going for smoking break...'
sleep 2
echo -e '\e[0;90m                 (  )/  '
echo -e '\e[0;90m                  )(/'
echo -e "\e[0;93m  ________________$g(/)"
echo -e "\e[0;93m ()__)____________$r))"
echo -e '\e[0m'
sleep 12
clear
echo -e '\e[96m almost there.. taking final puffs ...'
echo -e '\e[0;90m       ( )/  '
echo -e '\e[0;90m        )(/'
echo -e "\e[0;93m  ______$g(/)"
echo -e "\e[0;93m ()__)__$r))"
echo -e '\e[0m'
sleep 5
clear
echo -e '\e[96m tossing out cigarette butt...'
sleep 1 
clear
echo -e '\e[96m back to work..'
echo -e '\e[0m'  
sleep 2
clear
echo -e '\e[96m doing some paperworks for Regov (issuer) & Company (verifier)..'
echo -e '\e[0m' 
chmod +x init.sh
sleep 0.5 
xdotool type "chmod +x init.sh"
xdotool key KP_Enter
sleep 0.3
xdotool type "./init.sh"
xdotool key KP_Enter
sleep 0.3
xdotool type "regov"
xdotool key KP_Enter
sleep 0.3
xdotool type "regov"
xdotool key KP_Enter
sleep 0.3
xdotool type "regov"
xdotool key KP_Enter
sleep 0.3
xdotool type "2"
xdotool key KP_Enter
sleep 0.3
xdotool type "clear"
xdotool key KP_Enter
sleep 0.3
xdotool type "./init.sh"
xdotool key KP_Enter
sleep 0.3
xdotool type "company"
xdotool key KP_Enter
sleep 0.3
xdotool type "company"
xdotool key KP_Enter
sleep 0.3
xdotool type "company"
xdotool key KP_Enter
sleep 0.3
xdotool type "2"
xdotool key KP_Enter
sleep 0.3
xdotool type "clear"
xdotool key KP_Enter
echo -e '\e[0;33m starting both agents...'
echo -e '\e[0m'
xdotool type 'docker-compose -f docker-compose-regov.yml up --build' #start agent
xdotool key KP_Enter
xdotool key shift+ctrl+E
sleep 1
xdotool type 'docker-compose -f docker-compose-company.yml up --build'
xdotool key KP_Enter
xdotool key alt+Up
xdotool key shift+ctrl+E
sleep 1
xdotool type 'docker-compose -f docker-compose-webhook_2.yml up --build' #start company-controller
xdotool key KP_Enter
xdotool key alt+Left
xdotool key alt+Left
xdotool key shift+ctrl+o
sleep 1
xdotool type 'cd ..'
xdotool key KP_Enter
xdotool type 'cd indy-tails-server/docker'
xdotool key KP_Enter
xdotool type 'GENESIS_URL=http://localhost:9000/genesis ./manage start --logs'
xdotool key KP_Enter
sleep 1
echo -e '\e[0;33m starting both agents...'
echo -e '\e[0m'
terminator
clear
xdotool type "cd rnd-aries-wallet-part1"
xdotool key KP_Enter
xdotool type 'python3 regov.py'
xdotool key KP_Enter
xdotool key shift+ctrl+e
sleep 0.5
xdotool type 'python3 apple.py'
xdotool key KP_Enter
sleep 1
echo -e '\e[34m all done'
echo -e '\e[0m'






