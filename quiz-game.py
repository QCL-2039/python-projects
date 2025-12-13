import matplotlib.pyplot as plt

# ----------------------------
# QUIZ DATA
# ----------------------------

questions = (
    "1. What is the capital of France?",
    "2. Which language is used for web development?",
    "3. Who developed Python programming language?",
    "4. What does CPU stand for?",
    "5. Which one is a JavaScript framework?",
    "6. What is the largest planet in our solar system?",
    "7. Which data structure uses FIFO?",
    "8. What is the chemical symbol for Gold?",
    "9. Which device is used to store data permanently?",
    "10. Which protocol is used to transfer webpages?"
)

options = (
    ("A. Paris", "B. London", "C. Rome", "D. Berlin"),
    ("A. HTML", "B. SQL", "C. C++", "D. Bash"),
    ("A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Elon Musk"),
    ("A. Central Processing Unit", "B. Control Program Unit", "C. Computer Power Unit", "D. Core Process Utility"),
    ("A. Django", "B. React", "C. Angular", "D. TensorFlow"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. Stack", "B. Queue", "C. Tree", "D. Graph"),
    ("A. Au", "B. Ag", "C. Fe", "D. Go"),
    ("A. RAM", "B. SSD", "C. Cache", "D. Register"),
    ("A. FTP", "B. HTTP", "C. SMTP", "D. SSH")
)

answer_sheet = ("A", "A", "A", "A", "B", "C", "B", "A", "B", "B")

# ----------------------------
# QUIZ LOGIC
# ----------------------------

print("🎉 Welcome to the Quiz Game! 🎉")
print("----------------------------------\n")

start = input("Do you want to play this game? (yes/no): ")

if start.strip().lower() != "yes":
    print("\nYou quit the game. See you next time! 👋")
else:
    print("\nGreat! Let's start the quiz! 🚀\n")

    correct_answer = 0
    wrong_answer = 0

    question_no = 0

    for question in questions:
        print(question)
        for option in options[question_no]:
            print(option)

        user_answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

        if user_answer == answer_sheet[question_no]:
            print("✅ Correct!\n")
            correct_answer += 1
        else:
            print("❌ Wrong!")
            print("Correct answer is:", answer_sheet[question_no], "\n")
            wrong_answer += 1

        question_no += 1

    # ----------------------------
    # RESULTS
    # ----------------------------

    print("🎯 QUIZ COMPLETED!")
    print("----------------------------")
    print(f"✔ Correct Answers : {correct_answer}")
    print(f"✘ Wrong Answers   : {wrong_answer}")
    print(f"📊 Your Score     : {correct_answer}/10")
    print("----------------------------\n")

    # ----------------------------
    # PIE CHART
    # ----------------------------

    ratio_list = [correct_answer, wrong_answer]

    plt.title("Your Answer Ratio")
    plt.pie(
        ratio_list,
        autopct="%0.1f%%",
        shadow=True,
        colors=['green', 'red'],
        labels=["Correct Answers", "Wrong Answers"]
    )
    plt.show()
