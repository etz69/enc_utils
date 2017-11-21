#!/usr/bin/env bash
IN=$1
array=(${IN//=/ })

alert_id=${array[1]}

basename="$(dirname $0)"
env_loc="${basename}/socmonkey_standalone/p3env/bin/activate"
script_loc="${basename}/socmonkey_standalone"

source $env_loc
cd $script_loc
python analyzeoffense.py $alert_id