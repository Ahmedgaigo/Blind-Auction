from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")

end = False
Bid = {}

def find_highest_bid(record):
    highest_bid = 0
    winner =""
    for bidder in record:
        bid_amnt = record[bidder]
        if bid_amnt > highest_bid:
            highest_bid = bid_amnt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not end:
    bidder = input('\nWhat is your name?: ')
    bid = int(input('\nWhat is your bid?: $'))
    Bid[bidder] = bid
   
    any_bidders = input('\nAre there any other bidders? Type "yes" or "no": ').lower()    
        
    if any_bidders == "no":
        end = True
        find_highest_bid(Bid)
    elif any_bidders == "yes":
        clear()
