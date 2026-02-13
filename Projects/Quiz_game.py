import random

# Define questions as a list of dictionaries
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippo"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Dickens", "Hemingway", "Tolkien"],
        "answer": 0
    },
    {
        "question": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "answer": 2
    },
     {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": 1
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["90°C", "100°C", "120°C", "80°C"],
        "answer": 1
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Lungs", "Brain", "Heart", "Liver"],
        "answer": 2
    },
    {
        "question": "Which programming language is known for its snake logo?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": 2
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 2
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "options": ["India", "China", "Japan", "Egypt"],
        "answer": 1
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Control Panel Utility", "Core Programming Unit"],
        "answer": 0
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["Holi", "Diwali", "Eid", "Christmas"],
        "answer": 1
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Oxide", "Organium"],
        "answer": 1
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Ringgit"],
        "answer": 2
    }
]


# Shuffle the questions
random.shuffle(quiz_data)

# Define the quiz function
def run_mcq_quiz():
    score = 0
    print("🎯 Welcome to the MCQ Quiz!\n")

    for i, q in enumerate(quiz_data):
        print(f"Q{i+1}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"  {idx + 1}. {option}")
        try:
            user_input = int(input("Your answer (1-4): ")) - 1
            if user_input == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                correct_option = q['options'][q['answer']]
                print(f"❌ Wrong! Correct answer: {correct_option}\n")
        except ValueError:
            print("⚠️ Invalid input. Skipping question.\n")

    print(f"🏁 Quiz Finished! Your score: {score}/{len(quiz_data)}")

#Running the quiz
run_mcq_quiz()
