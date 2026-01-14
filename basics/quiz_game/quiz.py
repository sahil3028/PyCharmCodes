import json

# Load questions from JSON file
with open("questions.json", "r") as file:
    data = json.load(file)

score = 0
questions = data["questions"]

for q in questions:
    print(f"\nQ{q['id']}. {q['question']}")

    for key, value in q["options"].items():
        print(f"{key}. {value}")

    user_ans = int(input("Enter your answer: "))

    # Check answer
    if user_ans == q["correct_answer"]:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")
        print(f"Correct answer was option {q['correct_answer']}")

# Final score
print(f"\nYour final score: {score}/{len(questions)}")