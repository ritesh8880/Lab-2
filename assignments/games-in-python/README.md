# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Create a complete Hangman game in Python to practice string manipulation, loops, conditionals, and game state tracking.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game with a list of secret words and select one at random for the player to guess.

#### Requirements
Completed program should:

- Define a list of at least 10 possible words.
- Randomly choose a word at the start of each game using `random.choice()`.
- Initialize the hidden word display as underscores for each letter.

### 🛠️ Player Input and Guess Processing

#### Description
Allow the player to guess letters and update the game state based on correct or incorrect guesses.

#### Requirements
Completed program should:

- Prompt the player to input a single letter guess.
- Reveal correct letters in the hidden word display.
- Track and show guessed letters and remaining attempts.
- Ignore repeated guesses and prompt again without losing attempts.

### 🛠️ Win/Lose Conditions and Replay Option

#### Description
Determine when the game is won or lost and offer the player a chance to play again.

#### Requirements
Completed program should:

- End the game with a win message when the word is fully guessed.
- End the game with a lose message when attempts run out, revealing the secret word.
- Ask the player if they want to play again and restart or exit based on their response.

