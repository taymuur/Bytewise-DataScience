# Mini Projects in Python

## General Knowledge Quiz Game

```python 
print("Welcome to Taimur's Computer Quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's start")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is central processing unit.")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is graphics processing unit.")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is random access memory.")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect! The correct answer is power supply.")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "% result.")
```

## Number Guessing Game

```python 
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_ans(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}.")


def set_difficulty():
    level = input("Choose a difficulty, 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_ans(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess Again!")
game()
```

## Rock, Paper & Scissors

```python 
import random
USER_WINS = 0
COMP_WINS = 0

import random

input_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
if input_choice > 2 or input_choice < 0:
    print("You entered an invalid character. You lose!")
else:
    choices = ['rock', 'paper', 'scissors']
    print(choices[input_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[comp_choice])
    
    if comp_choice == input_choice:
        print("Draw")
        
    elif input_choice == 0 and comp_choice == 2:
        print("You Won!")
        
    elif input_choice == 2 and comp_choice == 0:
        print("You lost!")
        
    elif comp_choice > input_choice:
        print("You lost")
        
    elif input_choice > comp_choice:
        print("You Win")

```
