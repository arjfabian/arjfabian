#!/bin/bash

# Count the number of regular files in the current directory
answer=$(ls -l | grep ^- | wc -l)

echo "Welcome to the Guessing Game!"
echo ""

# Define a function to ask the user for their guess
function ask_for_number {
    read -p "Tell me, how many files you think there are in this directory? " number
    echo ""
}

# Loop continues as long as the user's guess is incorrect
while [[ $number -ne $answer ]]; do
    # Ask the user for their guess
    ask_for_number
    # The guess is too low
    if [[ $number -lt $answer ]]; then
        echo "Try with a higher number!"
    # The guess is too high
    elif [[ $number -gt $answer ]]; then
        echo "Try with a lower number!"
    # The guess is correct
    else
        echo "You guessed it! Congratulations! Here are the files:"
        echo ""
        ls -l | grep ^-
        echo ""
        echo "Goodbye!"
    fi
done

