quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    }
}
    
score = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("Enter your answer: ")
    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is " + value["answer"])
        print("Your score is " + str(score))
        print("\n")

print("Your final score is " + str(score))