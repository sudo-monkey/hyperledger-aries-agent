#!/bin/bash

sleep 0.5
xdotool type './manage down'
xdotool key KP_Enter
xdotool key alt+Right
xdotool key ctrl+c
xdotool key ctrl+c
xdotool key KP_Enter
xdotool key alt+Right
xdotool key ctrl+c
xdotool key ctrl+c
xdotool key KP_Enter
xdotool key alt+Down
xdotool key ctrl+c
xdotool key ctrl+c
xdotool key KP_Enter
xdotool key alt+Left
xdotool key ctrl+c
xdotool key ctrl+c
xdotool key KP_Enter
xdotool key alt+Left
xdotool key ctrl+c
xdotool key KP_Enter
xdotool type './manage down'
xdotool key KP_Enter
xdotool type 'docker rm webhook'
xdotool key KP_Enter
xdotool type 'docker rm webhook_2'
xdotool key KP_Enter
xdotool type 'docker rm Company'
xdotool key KP_Enter
xdotool type 'docker rm Regov'
xdotool key KP_Enter
exit