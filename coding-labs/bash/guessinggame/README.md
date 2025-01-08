# Guessing Game

* An assignment for the **'The Unix Workbench'** course
* **Author:** arjfabian 
* **Creation date:** 2021/01/01
* **Lines of code:** 25 

This is a simple Bash script that counts the total of files in the current directory (not counting subdirectories) and asks the user to guess this value. The user will know after each try if the guess was too low or too high. The program ends when the guess is correct.

**Note:** This script relies on the `ls`, `grep`, and `wc` commands.

**How to Play:**

1. **Run the script:** Execute the `guessinggame.sh` script in your terminal.

2. **Enter your guess:** When prompted, enter your guess for the number of regular files in the current directory.

3. **Receive feedback:** 

    - If your guess is too low, the script will prompt you to "Try with a higher number!"

    - If your guess is too high, the script will prompt you to "Try with a lower number!"

4. **Win the game:** Once you guess the correct number of files, the script will display the list of files and congratulate you.

