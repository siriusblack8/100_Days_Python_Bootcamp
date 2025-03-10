print("Welcome to 'BILL SPLIT' calculator")
bill = float(input("Enter your total amount: "))
tip = float(input("Enter how much you want to tip: "))
total = bill+tip
num = int(input("Enter how many people to be split among: "))
pay = round(total/num, 2)
print(f"Each person should pay {pay}")