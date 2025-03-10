

#ask name, ask bid
#store bid as value for the key, append it to a dictionary
#ask if more bidders
#if yes add 100 new lines, repeat above task 
#if no loop through the values of keys stored in the dictionary to find highest bid

def bidding():
    more_bids = 0
    biddings_details = {}
    while more_bids != True:
        name = input("What is your name? ")
        bid = input("what is your bid in $? ")
        biddings_details[name] = int(bid)
        more_bidders = (input("Are there more bidders?(Type yes/ no): ")).lower()
        if more_bidders == "yes":
            more_bids = 0
            print("\n"*100)
        else:
            more_bids = 1 
    print("\n"*100)
    highest_bid = 0  
    highest_bidder = ""
    for bidder in biddings_details:
        if biddings_details[bidder]> highest_bid:
            highest_bid = biddings_details[bidder]
            highest_bidder = bidder
    
    return(print(f"The highest bid is ${highest_bid} by {highest_bidder}"))

print("Welcome to silent bid!")
bidding()

