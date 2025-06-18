import random

def minus():
    x = 2
    y = 144
    while x <= y:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    return(f"{x} - {y}", x-y)

def plus():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return(f"{x} + {y}", x+y) 

while True:
    name = input("Please input your name: ")
    if name.isalpha() == True:
        break
    print("Invalid name")

while True:
    try:
        age = int(input("Please input your age: "))
        if age <= 10 and age >= 6:
            break
        else:
            print("Must input a number between 6 and 10")
    except ValueError:
        print("Must input a number between 6 and 10")



while True:
    operator = input("What questions would you like (+ or -) ")
    if operator == '+' or operator == '-':
        break
    print("Please input either + or -")

score = 0

for i in range(1, 6):
    if operator == '+':
        questionAnswer = plus()
    else:
        questionAnswer = minus()

    print(questionAnswer[0])
    while True:
        try:
            attempt = int(input("Answer: "))
            break
        except ValueError:
            print("Answer must be a number")

    if attempt == questionAnswer[1]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

print(f"you scored {score} out of 5!")