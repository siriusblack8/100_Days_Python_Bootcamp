def making_coffee(total_resource,order_resources,money):
    total_resource["Water"]-=order_resources["Water"]
    total_resource["Coffee"]-=order_resources["Coffee"]
    total_resource["Milk"]-=order_resources["Milk"]
    total_resource["Money"]+= order_resources["Money"]
    balance = money-order_resources["Money"]
    print(f"Here is your change ${balance}")
    print("\n")
    return (total_resource)
    
def report(a):
    print(f"Water: {a["Water"]}ml")
    print("\n")
    print(f"Coffee: {a["Coffee"]}g")
    print("\n")
    print(f"Milk: {a["Milk"]}ml")
    print("\n")
    print(f"Money: ${a["Money"]}")
    print("\n")
    
def Money_calculation():
    print("Please input money in coins")
    print("\n")
    amount_paid = 0
    value_coins = {"quarters":0.25 , "dimes":0.10 , "nickles":0.05 , "pennies":0.01}
    for coins in value_coins:
        count = int(input(f"Enter how many {coins}: "))
        print("\n")
        amount_paid += count*value_coins[coins]
    return(amount_paid)
    
def resource_sufficiency(total_resource,order_resources,money):
    if total_resource["Water"]<order_resources["Water"]:
        print("Sorry, there is not enough water! Money refunded")
        print("\n")
        return False
    if total_resource["Coffee"]<order_resources["Coffee"]:
        print("Sorry, there is not enough coffee! Amount refunded")
        print("\n")
        return False
    if total_resource["Milk"]<order_resources["Milk"]:
        print("Sorry, there is not enough milk! Money refunded")
        print("\n")
        return False
    if money<order_resources["Money"]:
        print("Amount not enough! Money refunded ")
        print("\n")
        return False
    return True
    
def coffee_machine():
    resources = {"Milk": 1000 , "Coffee": 500 , "Water": 2500, "Money": 100 }
    cont = 1
    while cont == 1:
        customer_input = (input("What would you like to order? (americano/latte/cappuccino):")).lower()
        resources_required = {
            "americano": {"Milk":0 , "Coffee": 60 , "Water": 120, "Money":2.39 }, 
            "latte": {"Milk": 170, "Coffee": 30 , "Water":30, "Money":4.52 }, 
            "cappuccino":{"Milk": 140 , "Coffee":60 , "Water": 60, "Money":8.71 }
        }
        
        if customer_input == "off":
            print("Turning off machine...")
            cont = 0
            return
        elif customer_input == "report":
            print("\n")
            report(resources)
        else:
            amount_paid = Money_calculation()
            if resource_sufficiency(resources, resources_required[customer_input], amount_paid) == True:
                print(f"Making your {customer_input}")
                print(f"Here is your {customer_input}")
                print("\n")
                resources = making_coffee(resources,resources_required[customer_input],amount_paid )
            else:
                print("Order Cancelled")
            
coffee_machine()