import random

def get_random_quote():
    """Get a random quote from the list."""
    quotes = [
        "Be yourself; everyone else is already taken. - Oscar Wilde",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Don't count the days, make the days count. - Muhammad Ali",
        "The best way to predict the future is to create it. - Peter Drucker",
        "Happiness is not something readymade. It comes from your own actions. - Dalai Lama",
    ]
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    input("Press Enter to get a random quote...")
    while True:
        quote = get_random_quote()
        print("\n" + quote)
        try_again = input("\nDo you want another quote? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thanks for using the Random Quote Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
