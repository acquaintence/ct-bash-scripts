#! /bin/bash
prompt=true 

while $prompt
do
    read -p "Would you like to play Rock Paper Scissors?: [y/n] " answer 

    if [[ $answer == [Yy] ]]; then
        python3 rps_game.py
        prompt=false
    elif [[ $answer == [Nn] ]]; then
        echo "That's too bad, maybe next time."
        prompt=false
    else
        echo "Invalid response. Please select y / n"
    fi
done