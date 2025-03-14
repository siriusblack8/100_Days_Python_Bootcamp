def making_coffee(total_resource,order_resources,money):
    """changes the resources available after processing the order"""
    total_resource["Water"]-=order_resources["Water"]
    total_resource["Coffee"]-=order_resources["Coffee"]
    total_resource["Milk"]-=order_resources["Milk"]
    total_resource["Money"]+= order_resources["Money"]
    balance = money-order_resources["Money"]
    print(f"Here is your change ${balance}")
    print("\n")
    return (total_resource)
    
def report(a,b):
    """give a report on resources available"""
    print(f"Water: {a["Water"]}ml")
    print(f"Coffee: {a["Coffee"]}g")
    print(f"Milk: {a["Milk"]}ml")
    print(f"Money: ${a["Money"]}")
    print(f"Profit: ${a["Money"]- b}")
    print("\n")
    
def Money_calculation():
    """calculates the total amount input by the user"""
    print("Please input money in coins")
    print("\n")
    amount_paid = 0
    value_coins = {"quarters":0.25 , "dimes":0.10 , "nickles":0.05 , "pennies":0.01}
    for coins in value_coins:
        count = int(input(f"Enter how many {coins}: "))
        amount_paid += count*value_coins[coins]
    print("\n")
    return(amount_paid)
    
def resource_sufficiency(total_resource,order_resources,money):
    """checks if the resources are sufficient for the order placed"""
    for items in total_resource:
        if total_resource[items]<order_resources[items]:
            print(f"Sorry, there is not enough {items}! Money refunded")
            print("\n")
            return False
    if money<order_resources["Money"]:
        print("Amount not enough! Money refunded ")
        print("\n")
        return False
    return True
    
def coffee_machine():
    resources = {"Milk": 1000 , "Coffee": 500 , "Water": 2500, "Money": 100 }
    initial_amount = resources["Money"]
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
            report(resources, initial_amount)
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
