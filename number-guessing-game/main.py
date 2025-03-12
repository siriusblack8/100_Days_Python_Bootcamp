import random
I = random.randint(1,100)

def guess_num(a):
    print(f"You have got {a} guesses in total!")
    chances = a
    for i in range (0,a):
        num = int(input("Guess a number: "))
        if num == I:
            print("You are right, that is the number!")
            return
        elif num>I:
            print("Too High! Guess again")
            chances -=1
            print(f"You have {chances} turns left")
            
        elif num<I:
            print("Too Low! Guess again")
            chances -=1
            print(f"You have {chances} turns left")
            
        elif chances == 0:
            print("No more chances left. You Lose!")
            print(f"The number is {I}")


print("Welcome to the 'Number Guessing Game!'")
print("Guess the number I am thinking of...")
print("Your first clue - it is between 1 and 100")
level = (input("What level do you want to try? Type 'easy' or 'hard': ")).lower()
if level == "easy":
    guess_num(10)
elif level == "hard":
    guess_num(5)