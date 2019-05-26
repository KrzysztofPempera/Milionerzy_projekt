import random


answers = ["a","b","c","d"]
correct_answer_index = 0

def fifty_fifty():
    correct_answer = answers[correct_answer_index]

    answers.remove(answers[correct_answer_index])
    
    second_answer = answers[random.randint(0,2)]    

    new_answers = []

    new_answers.append(correct_answer)
    new_answers.append(second_answer)

    print(new_answers)

def phone():
    correct_chance = random.randint(0,100)

    if correct_chance>40:
        print(answers[correct_answer_index])
    elif correct_chance<60:
        print(answers[random.randint(0,2)])

def public():
    percentage = 100
    for i in range(len(answers)):
        n = random.randrange(percentage)
        print(n,"% publiczności, twierdzi że odpowiedź ",answers[i]," jest poprawna")
        percentage = percentage - n
##fifty_fifty()
##phone()
##public()
