
# assign 1st to a and 2nd to b
# compare the follower for both and whichever is the highest store its corresponding letter (a or b) it in high variable. 
# display a and b, with name and details and ask user to choose between a and b
# if user chose correct, keep the 2nd one in a and generate a new person in b. add one point to user
# repeat the abve step until the user chooses wrong
# if wrong, display - you lost and the points scored by the user

import data
import random

def data_display(a,b):
    print(f"Celebrity A is {a[0]}, {a[1]['description']}")
    print(f"Celebrity B is {b[0]}, {b[1]['description']}")
    
def highest_count(a,b):
    a_count = a[1]["follower_count"]
    b_count = b[1]["follower_count"]
    if (a_count)>(b_count):
        return("a")
    return("b")

def High_Low():
    data_list = list(data.celebrity_data.items())
    first_id = random.choice(data_list)
    second_id = random.choice(data_list)
    cont = 1
    points = 0
    while cont == 1:
        data_display(first_id, second_id)
        user_answer = (input("Who has more followers? A or B ")).lower()
        if user_answer == highest_count(first_id, second_id):
            points+=1
            print("You are right!")
            print(f"{first_id[0]} has {first_id[1]["follower_count"]} followers")
            print(f"{second_id[0]} has {second_id[1]["follower_count"]} followers")
            print(f"Point scored - {points}")
            print("\n")
            first_id = second_id
            second_id = random.choice(data_list)
            
        else:
            print("You are wrong!")
            print(f"{first_id[0]} has {first_id[1]["follower_count"]} followers")
            print(f"{second_id[0]} has {second_id[1]["follower_count"]} followers")
            print(f"Point scored - {points}")
            cont = 0
        
print("Guess High or Low!")
print("\n")
High_Low()