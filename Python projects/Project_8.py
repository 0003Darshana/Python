import random

def get_random_joke():
    """Get a random joke from the list."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some fish play piano? You can't tuna fish!",
        "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
        "What did one hat say to the other hat? You stay here, I'll go on ahead!",
        "Why do we never trust stairs? They're always up to something!",
        "Why did the tomato turn red? Because it saw the salad dressing!"
    ]
    return random.choice(jokes)

def main():
    print("Welcome to the Random Joke Generator!")
    input("Press Enter to get a random joke...")
    while True:
        joke = get_random_joke()
        print("\n" + joke)
        try_again = input("\nDo you want another joke? (yes/no): ").lower()
        if try_again != 'yes':
            print(f"Thanks for using the Random Joke Generator. Goodbye{chr(128516)}!")
            break

if __name__ == "__main__":
    main()
