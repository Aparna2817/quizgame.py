# Define the quiz questions, options, and correct answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Mark Twain", "B. J.K. Rowling", "C. Harper Lee", "D. Jane Austen"],
        "answer": "C"
    }
]

def ask_questions(quiz_questions):
    score = 0
    
    for item in quiz_questions:
        question = item["question"]
        options = item["options"]
        correct_answer = item["answer"]
        
        # Display the question and options
        print("\n" + question)
        for option in options:
            print(option)
        
        # Get user answer with input validation
        user_answer = input("Please enter the letter of your answer: ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Please enter the letter of your answer: ").strip().upper()
        
        # Check the answer and provide feedback
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    return score

def display_score(score, total_questions):
    print(f"\nYour final score is {score} out of {total_questions}.")

def run_quiz():
    total_questions = len(quiz_questions)
    score = ask_questions(quiz_questions)
    display_score(score, total_questions)

# Run the quiz
if __name__ == "__main__":
    run_quiz()
