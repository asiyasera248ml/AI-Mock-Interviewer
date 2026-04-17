# AI Mock Interviewer (Enhanced Offline Version)

import random

questions = [
    "Tell me about yourself",
    "What is Java?",
    "Explain OOP concepts",
    "What are your strengths?",
    "What is polymorphism?",
    "Why should we hire you?"
]

total_score = 0

print("🤖 AI Mock Interview Started!\n")

for q in questions:
    print("Question:", q)
    answer = input("Your Answer: ")

    print("\nAI Feedback:")

    score = 0

    # Smarter evaluation
    if len(answer.strip()) == 0:
        score = 0
        print("❌ You didn't answer the question.")
    elif len(answer) < 20:
        score = 5
        print("⚠️ Answer is too short. Add more explanation.")
    elif any(word in answer.lower() for word in ["example", "for instance", "like"]):
        score = 9
        print("🌟 Great! You used examples.")
    elif any(word in answer.lower() for word in ["because", "so", "therefore"]):
        score = 8
        print("👍 Good explanation and reasoning.")
    elif len(answer) > 60:
        score = 8
        print("👍 Detailed answer, well done.")
    else:
        score = 7
        print("✔️ Decent answer, but can be improved.")

    total_score += score

    print(f"Score: {score}/10")

    # Smart suggestion based on question
    print("\nBetter Answer Suggestion:")

    if "java" in q.lower():
        print("Java is a high-level, object-oriented programming language used for building applications. Example: Android apps.")
    elif "oop" in q.lower():
        print("OOP includes concepts like Encapsulation, Inheritance, Polymorphism, and Abstraction with real-life examples.")
    elif "strength" in q.lower():
        print("Mention 2-3 strengths with examples, like teamwork, problem-solving.")
    elif "hire" in q.lower():
        print("Explain your skills, willingness to learn, and how you add value to the company.")
    else:
        print("Include introduction, key points, and a real-life example.")

    print("\n" + "-"*50 + "\n")

# Final result
average = total_score / len(questions)

print("✅ Interview Finished!")
print(f"Your Average Score: {average:.2f}/10")

# Final evaluation
if average >= 8:
    print("🌟 Excellent performance! You are interview-ready.")
elif average >= 6:
    print("👍 Good performance, but practice more for perfection.")
else:
    print("⚠️ Needs improvement. Work on your answers and confidence.")