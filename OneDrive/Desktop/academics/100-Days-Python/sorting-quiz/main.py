print("Welcome young witch/wizard to the sorting quiz!")
print("Now, place the hat upon your head, and answer its questions honestly. Let the magic begin!")
x = 0
y = 0
answer1 = input("You are put in a hidden room filled with wondrous artifacts. Which one draws you in first? \n 'A' - A dusty tome filled with cryptic symbols.\n 'B' - A gleaming sword radiating an aura. \n 'C' - A golden cup overflowing with plump, juicy seeds. \n 'D' - A beautiful locket with an inscription in a strange language. \n")
if answer1 == "A":
    x+=1 
    y-=1 
elif answer1 =="B":
    x-=1 
    y+=1 
elif answer1 == "C":
    x-=1 
    y-=1 
elif answer1 == "D":
    x+=1 
    y+=1 
print("\n")
print("Hmm....A complex mind you have, answer this")
answer2 = input("The chamber leads to a pathway at the end of which there is a treasure box, Which treasure do you choose? \n 'A' - A scroll whispering secrets \n 'B' - A gleaming feather \n 'C' - A moonlit stone \n 'D' - A jeweled box with hidden message\n")
if answer2 == "A":
    x+=1 
    y-=1 
elif answer2 =="B":
    x-=1 
    y+=1 
elif answer2 == "C":
    x-=1 
    y-=1 
elif answer2 == "D":
    x+=1 
    y+=1 
print("\n")
print("Let's delve deeper.")
answer3 = input("As you move forward you stand at a crossroad which path do you take? \n 'A' - A dust chamber filled with forgotten tools and alchemy equipment \n 'B' - A stone bridge leading to a churning chasm \n 'C' - A room filled with sunlight and mismatched armchairs \n 'D' - A dimlit corridor \n")
if answer3 == "A":
    x+=1 
    y-=1 
elif answer3 =="B":
    x-=1 
    y+=1 
elif answer3 == "C":
    x-=1 
    y-=1 
elif answer3 == "D":
    x+=1 
    y+=1
print("\n")
print("Interesting, you seem quite comfortable on this path.")
answer4 = input("If given a choice which would you rather face? \n 'A' - A whispering willow \n 'B' - A moonlit maze full of challenges \n 'C' - Playful pixies \n 'D' - A whimsical treasure hunt \n")
if answer4 == "A":
    x+=1 
    y-=1 
elif answer4 =="B":
    x-=1 
    y+=1 
elif answer4 == "C":
    x-=1 
    y-=1 
elif answer4 == "D":
    x+=1 
    y+=1
print("\n")
print("Just one more question, young witch or wizard. Then, we'll reveal your destiny!")
answer5 = input("Deep inside which house do you really want to be in? \n 'A' - Ravenclaw \n 'B'- Gryffindor \n 'C' - Hufflepuff \n 'D'- Slytherin \n")
if answer5 == "A":
    x+=1 
    y-=1 
elif answer5 =="B":
    x-=1 
    y+=1 
elif answer5 == "C":
    x-=1 
    y-=1 
elif answer5 == "D":
    x+=1 
    y+=1
if x>0 and y>0:
    print("Ambition and cunning are powerful tools. Use them wisely, and you'll find great success in \n 'SLYTHERIN'.")
elif x<0 and y>0:
    print(" Brave one, join the ranks of the daring and the chivalrous! Remember, courage doesn't always roar.\n 'GRYFFINDOR'")
elif x<0 and y<0:
    print("Loyalty, dedication, and kindness. You'll find a true home here in \n 'HUFFLEPUFF'.")
elif x>0 and y<0:
    print("Welcome to the house of wit and learning. May your thirst for knowledge never be quenched. \n 'RAVENCLAW'")
else:
    print("I think you have not been entirely honest, take the quiz again")