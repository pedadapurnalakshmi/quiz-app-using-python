# quiz_app.py

# Quiz questions data (can also be loaded from JSON or CSV)
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which language is primarily used for Android app development?",
        "options": ["A. Java", "B. Python", "C. Swift", "D. Kotlin"],
        "answer": "D"
    },
    {
        "question": "Who developed Python programming language?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "What is the value of 3 ** 2?",
        "options": ["A. 5", "B. 6", "C. 9", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a Python data type?",
        "options": ["A. Integer", "B. String", "C. List", "D. All of the above"],
        "answer": "D"
    }
]

def run_quiz(questions):
    score = 0
    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🎉 Quiz Complete! Your score: {score} out of {len(questions)}")

# Run the app
if __name__ == "__main__":
    print("=== Welcome to the Python Quiz App ===")
    run_quiz(quiz_questions)
