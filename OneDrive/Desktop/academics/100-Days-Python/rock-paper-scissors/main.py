import random
print("Welcome to rock, paper, scissors!")
user = input("What do you choose? Rock, Paper or Scissors?")
user = user.lower()
user_list = ['rock', 'paper', 'scissors']
user_index = user_list.index(user)
ran = random.randint(0,2)
if ran == 0:
    print("Computer choose Rock")
elif ran == 1:
    print("Computer choose Paper")
elif ran == 2:
    print("Computer choose Scissors")

if user_index == ran:
    print("Draw!")
elif user_index == 0:
    if ran == 1:
        print("You lost!")
    else:
        print("You won!")
elif user_index == 1:
    if ran == 2:
        print("You lost!")
    else:
        print("You won!")
elif user_index == 2:
    if ran == 1:
        print("You lost!")
    else:
        print("You won!")