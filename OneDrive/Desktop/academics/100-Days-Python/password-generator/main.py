import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
x = int(input("Enter how many letters you need in your password: "))
y = int(input("Enter how many numbers you need in your password: "))
z = int(input("Enter how many symbols ou need in your password: "))

password = ''
(l,n,s) = (0,0,0)
for i in range (x+y+z+1):
    p = random.randrange(1,4)
    if p==1 and l<x+1:
        letter = str(letters[random.randrange(0,len(letters))])
        password = password + letter 
        l +=1 
    elif p==2 and l<y+1:
        number = str(numbers[random.randrange(0,len(numbers))])
        password = password + number 
        n +=1
    elif p==3 and l<z+1:
        symbol = str(symbols[random.randrange(0,len(symbols))])
        password = password + symbol 
        s +=1    
print("Password is " + password)
