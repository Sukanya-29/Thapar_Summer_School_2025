# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word from a list of words and allows the player to guess the letters in the word. The game provides visual feedback using hangman stages, showing the player's progress and how many tries are left.

There are 2 files: [hangman.py](https://github.com/Sukanya-29/Hangman_Game/blob/main/hangman.py) is a python file code with gui and [MiniProject_Hangman_game.ipynb](https://github.com/Sukanya-29/Hangman_Game/blob/main/MiniProject_Hangman_game.ipynb) is a google colab notebook with code only.

## How to Play

* The game randomly selects a word from the `words.txt` file.
* The player guesses letters one by one.
* If the guessed letter is in the word, it is revealed in the correct positions.
* If the guessed letter is not in the word, a part of the hangman is drawn.
* The player has a limited number of tries (6 by default) to guess the word.
* The game ends when the player guesses the word correctly or runs out of tries.
