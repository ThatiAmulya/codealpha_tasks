import random

# Words for the game
words = ["python", "computer", "programming", "developer", "robot"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Number of attempts
attempts = 6

# Store guessed letters
guessed_letters = []

print("================================")
print("        HANGMAN GAME")
print("================================")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    # Wrong guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You won!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)