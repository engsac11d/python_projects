#Python quiz game

questions = ("What is the smallest prime number?: ",
             "What is the largest internal organ in the human body?: ",
             "Which gas do plants absorb from the atmosphere? ",
             "How many hearts does an octopus have?: ",
             "What is a group of lions called?: ")


options = (("A. Three", "B. two", "C. four", "D. five"),
           ("A. heart", "B. lungs", "C. liver", "D. brain"),
           ("A. oxygen", "B. nitrogen", "C. hydrogen", "D.carbon dioxide"),
           ("A. one", "B. two", "C. three", "D. four"),
           ("A. pack", "B. pride", "C. herd", "D. school" ))

answers = ("B", "C", "D", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)
      

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")

    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("------------------------")
print("        RESULT          ")
print("------------------------")
      
print("answers: ", end="")
for answer in answers:
    print(answer, end =" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score =int(score /len(questions) * 100)
print(f"your score is: {score}%")




    