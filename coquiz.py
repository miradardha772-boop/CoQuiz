# CoQuiz Game

def play_quiz():
    # Initialize the score tracker
    score = 0
    
    # Define questions, options, and correct answers
    questions = [
        {
            "prompt": "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\nYour answer: ",
            "answer": "b"
        },
        {
            "prompt": "Which planet is known as the Red Planet?\n(a) Venus\n(b) Mars\n(c) Jupiter\nYour answer: ",
            "answer": "b"
        },
        {
            "prompt": "What is 5 + 7?\n(a) 10\n(b) 12\n(c) 14\nYour answer: ",
            "answer": "b"
        },
        {
            "prompt": "Which language is primarily used for web styling?\n(a) Python\n(b) HTML\n(c) CSS\nYour answer: ",
            "answer": "c"
        },
        {
            "prompt": "Who is the 7th Hokage from the anime Naruto?\n(a) Naruto Uzumaki\n(b) Sasuke Uchiha\n(c) Minato Uzumaki\nYour answer: ",
            "answer": "a"
        },
        {
            "prompt": "What is the capital of Lithuania?\n(a) Montenegro\n(b) Paris\n(c) idk either\nYour answer: ",
            "answer": "c"
        },
        {
            "prompt": "Am I an expert at coding?\n(a) YES\n(b) Meh, not so much\n(c) No, wrong answer\nYour answer: ",
            "answer": "a"
        }
    ]

    print("Welcome to CoQuiz! Test your knowledge.\n")

    # Loop through each question using a for loop
    for index, q in enumerate(questions, start=1):
        print(f"--- Question {index} ---")
        # Get user input, remove extra spaces, and convert to lowercase
        user_answer = input(q["prompt"]).strip().lower()
        
        # Check the answer using if/else
        if user_answer == q["answer"]:
            print("Correct! 🎉\n")
            score += 1  # Increment score tracking
        else:
            print(f"Incorrect. The correct answer was ({q['answer']}).\n")

    # Display final results
    print("=" * 30)
    print("Quiz Over!")
    print(f"Your final score is: {score} out of {len(questions)}")
    
    # Calculate percentage
    percentage = (score / len(questions)) * 100
    print(f"You scored: {percentage:.0f}%")
    print("=" * 30)

# Run the game
if __name__ == "__main__":
    play_quiz()
