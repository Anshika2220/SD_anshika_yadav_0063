questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A. Lyon", "B. Paris", "C. Nice", "D. Marseille"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["A. Munich", "B. Hamburg", "C. Berlin", "D. Frankfurt"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Osaka", "B. Kyoto", "C. Tokyo", "D. Nagoya"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Uttar Pradesh?",
        "options": ["A. Kanpur", "B. Agra", "C. Lucknow", "D. Varanasi"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Rajasthan?",
        "options": ["A. Jaipur", "B. Udaipur", "C. Jodhpur", "D. Kota"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["A. Pune", "B. Mumbai", "C. Nagpur", "D. Nashik"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Gujarat?",
        "options": ["A. Ahmedabad", "B. Surat", "C. Vadodara", "D. Gandhinagar"],
        "answer": "D"
    },
    {
        "question": "What is the capital of Karnataka?",
        "options": ["A. Bengaluru", "B. Mysuru", "C. Hubballi", "D. Mangaluru"],
        "answer": "A"
    }
]

score = 0

print("====== Capitals Quiz ======\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer: {q['answer']}\n")

print("====== Quiz Finished ======")
print(f"Your Score: {score}/{len(questions)}")
print(f"Percentage: {(score/len(questions))*100:.2f}%")