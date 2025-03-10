def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)
    
def mul(a,b):
    return (a*b)
    
def div(a,b):
    if b == 0:
        return "Error! Division by zero."
    return (a/b)
    
def calculator():
    while True:
        num1 = int(input("Enter a number: "))
        cont_boolean = True
        while cont_boolean is True:
            operation = input("Enter an operation to be performed: (+  -  *  /) ")
            num2 = int(input("Enter the second number: "))
            operations = {"+": add, "-": sub, "*": mul, "/": div}
            result = operations[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")
            cont = input(f"Do you want to continue operation with {result}? (Type y if yes and n if no) ")
            if cont == "y":
                cont_boolean = True
                num1 = result
            else:
                cont_boolean = False

print("Calculator")
calculator()