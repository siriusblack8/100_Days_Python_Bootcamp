import random

def random_card_selection():
    cards = {"A":1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    random_pair = random.choice(list(cards.items()))
    return (random_pair)
    
def total_card_value(a,b):
    value = sum(a)
    ace_count = b.count("A")
    if value+10<=21 and ace_count>0:
        value+=10
    return(value)

def blackjack(): 
    user_deal= []
    dealer_deal = []
    user_cards = []
    dealer_cards = []
    
    user_card1, user_card1_value = random_card_selection()
    user_deal.append(user_card1_value)
    user_cards.append(user_card1)
    print(f"Your card 1 is {user_card1}")
    
    dealer_card1, dealer_card1_value = random_card_selection()
    dealer_deal.append(dealer_card1_value)
    dealer_cards.append(dealer_card1)
    print(f"Dealer's card 1 is {dealer_card1}")
    
    user_card2, user_card2_value = random_card_selection()
    user_deal.append(user_card2_value)
    user_cards.append(user_card2)
    print(f"Your card 2 is {user_card2}")
    
    dealer_card2, dealer_card2_value = random_card_selection()
    dealer_deal.append(dealer_card2_value)
    dealer_cards.append(dealer_card2)
    
    user_deal_value = total_card_value(user_deal, user_cards)
    dealer_deal_value = total_card_value(dealer_deal, dealer_cards)
    
    if user_deal_value == 21:
        print(user_cards)
        print("BlackJack! You Win!")
        return
    
    while user_deal_value <21:
        cont = input("Would you like to draw a card? If yes type y else type n: ")
        if cont == 'y':
            user_card, user_card_value = random_card_selection()
            user_deal.append(user_card_value)
            user_cards.append(user_card)
            user_deal_value = total_card_value(user_deal, user_cards)
            print(f"You have drawn the card {user_card}")
            print(f"Your deal at hand is {user_deal}")
        else:
            print(f"Your deal at hand is {user_deal}")
            break
        
    if user_deal_value>21:
        print(user_cards)
        print("Bust! You Lose")
        return
    
    if dealer_deal_value == 21:
        print(dealer_cards)
        print("BlackJack! Dealer Wins!")
        return
    
    while dealer_deal_value<=16:
        dealer_card, dealer_card_value = random_card_selection()
        dealer_deal.append(dealer_card_value)
        dealer_cards.append(dealer_card)
        dealer_deal_value = total_card_value(dealer_deal, dealer_cards)
               
    if dealer_deal_value>21:
        print(dealer_cards)
        print(f"Dealer scored {dealer_deal_value}.Dealer Bust! You Win!")
        return
                
    elif dealer_deal_value>user_deal_value:
        print(f"Dealer cards - {dealer_cards}")
        print(f"User cards - {user_cards}")
        print(f"Dealer scored {dealer_deal_value}, Dealer Wins!")
        return
        
    elif dealer_deal_value<user_deal_value:
        print(f"Dealer cards - {dealer_cards}")
        print(f"User cards - {user_cards}")
        print(f"You scored {user_deal_value}, You Win!")
        return
    
print("Welcome to Blackjack!")
blackjack()