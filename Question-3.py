import csv

with open ('my_quiz.csv') as file:
    do = csv.reader(file)
    questions = []
    answers = []
    for i in do:
        questions.append(i[0])
        answers.append(i[1])

name = input("Write Your name: ")

count = 0

for i in range(len(questions)):
    answer = input(questions[i] + " ")
    if answer.lower() == answers[i].lower():
        print("correct")
        count += 1
    else:
        print("Incorrect answer !")    
            
print("YOU got :", count)

with open ('my_quiz_results.csv', mode = 'a') as file:
    do = csv.writer(file)
    do.writerow([name, count])            
            