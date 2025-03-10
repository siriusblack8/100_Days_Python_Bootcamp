print("Welcome to The Rollercoaster!")
height = float(input("Please enter your height in cm: "))
if height>120:
    print("Congratulations! You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))
    if age<12:
        print("Cost of Child ticket Rs.75")
        bill = 75
    elif age<18:
        print("Cost of Youth ticket Rs.100")
        bill = 100
    else:
        print("Cost of Adult ticket Rs.150")
        teacher = input("Are you a teacher? Press Y or N: ")
        bill = 150
    photo = input("Do you want photo of you riding? Press Y or N: ")
    if photo == "Y" and teacher == "N":
        print("Cost of photo is Rs.30")
        bill+=30
        print(f"Your ticket bill is Rs. {bill}")
    elif photo == "Y" and teacher == "Y":
        print("Happy Teachers' Day! Cost of photo is Rs.0")
        bill+=0
        print(f"Your ticket bill is Rs. {bill}")
    elif photo == "N" and teacher == "Y":
        print("Happy Teachers' Day! Discount of Rs.30")
        bill-=30
        print(f"Your ticket bill is Rs. {bill}")
    else:
        print(f"Your ticket bill is Rs. {bill}")
else:
    print("Sorry you can't ride the rollercoaster :(")
  
