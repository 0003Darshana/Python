import random

def coin_toss():
    """Simulate a coin toss."""
    return random.choice(['Heads', 'Tails'])

def main():
    print("Welcome to the Coin Toss Game!")
    while True:
        guess = input("Enter your guess (Heads/Tails): ").capitalize()
        if guess not in ['Heads', 'Tails']:
            print("Invalid input. Please enter 'Heads' or 'Tails'.")
            continue
        result = coin_toss()
        print("Tossing the coin... It's", result + "!")
        if guess == result:
            print("Congratulations! Your guess was correct!")
        else:
            print("Oops! Better luck next time!")
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Thanks for playing the Coin Toss Game. Goodbye {chr(128516)}!")
            break

if __name__ == "__main__":
    main()
