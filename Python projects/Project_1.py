import random
questions = {

    "What is the capital of France?": "Paris",
    "What is the chemical symbol for water?": "H2O",
    "What is 188 / 4?": "47",
    "What is the largest planet in our solar system?": "Jupiter",
    "What country has the most islands?": "Sweden - 270,000",
    "Who is the author of the famous play 'Death of a Salesman' ": "Arthur Miller",
    "Which two elements make up the majority of the Earth's crust?": "Oxygen and Silicon",
    "What is the name of the instrument used to measure atmospheric pressure?": " Barometer",
    "Which scientist is credited with formulating the laws of motion and universal gravitation?": "Sir Isaac Newton",

}
def get_random_question():
    return random.choice(list(questions.keys()))

def play_trivia_quiz():
    score = 0
    total_questions = 5 
    print("Welcome to Trivia Quiz!")
    print("Answer the following questions:\n")
    for _ in range(total_questions):
        question = get_random_question()
        answer = questions[question]
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}\n")
    print("Quiz complete!")
    print(f"You scored {score}/{total_questions}")
if __name__ == "__main__":
    play_trivia_quiz()
