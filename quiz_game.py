print("Welcome to the Quiz Game!")

#List of questions and correct answers
quiz = [
    {"question": "Which programming language is known for its use in AI and Machine Learning?", "answer": "python"},
    {"question": "What is the full form of 'IDE' in software development?", "answer": "integrated development environment"},
    {"question": "Which technology is primarily used for building decentralized applications?", "answer": "blockchain"},
    {"question": "Which Python library is commonly used for data analysis and manipulation? ", "answer": "pandas"},
    {"question": "Which company provides the cloud service known?", "answer": "amazon"},
    {"question": "Which sorting algorithm has a time complexity of O(n log n) on average? ", "answer": "merge sort"},
    {"question": "Which SQL clause is used to filter records after the WHERE clause? ", "answer": "having"},
    {"question": "Which encryption algorithm is commonly used for securing web traffic? ", "answer": "ssl"}
]

score = 0 # initialize score

#loop through each question
for q in quiz:
    user_answer = input(q["question"]).lower()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer'].capitalize()}\n")

#Show result
print("Quiz Completed!\n")
print(f"You got {score} out of {len(quiz)} questions correct.")
percentage = (score / len(quiz)) * 100
print(f"Your score: {percentage:.2f}%")