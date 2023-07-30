import random

def choose_word():
    """Choose a random word from a list."""
    words = ["apple", "banana", "orange", "grape", "cherry", "strawberry", "watermelon", "pineapple"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    word_set = set(word)
    guessed_letters = set()
    attempts = 6
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("You have 6 attempts.")
    while attempts > 0:
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(display_word))
        if set(display_word) == word_set:
            print("Congratulations! You guessed the word:", word)
            break
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word_set:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess. Attempts remaining:", attempts)
    else:
        print("Game over! The word was:", word)

if __name__ == "__main__":
    play_hangman()
