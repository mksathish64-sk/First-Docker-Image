import random

words = ["python", "docker", "computer", "hangman", "programming"]
word = random.choice(words)

# Create the initial display with first and last letters revealed
guessed = ["_"] * len(word)
guessed[0] = word[0]          # Reveal first letter
guessed[-1] = word[-1]        # Reveal last letter

attempts = 6

print("Welcome to Hangman! The first and last letters are revealed.")
print("Word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
        continue

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    print("Word:", " ".join(guessed))

if "_" not in guessed:
    print(f"Congrats! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
