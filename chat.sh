#!/bin/bash
clear
xdotool key shit+ctrl+O
clear
xdotool type 'watch -n 0.1 cat webhooks/cache.txt'
xdotool key KP_Enter
