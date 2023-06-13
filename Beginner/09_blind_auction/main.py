# from replit import clear # If not using replit
import os
from art import logo


def clear():
    os.system('clear')


print(logo)
# HINT: You can call clear() to clear the output in the console.
auction_bids = {}
do_auction = True


def check_winner(auction_bids):
    max_val = 0
    winner = ''
    for key, value in auction_bids.items():
        if value >= max_val:
            max_val = value
            winner = key
    print(f"The winner is {winner} with a bid of ${max_val}")


while do_auction:
    bidder_name = str(input('What is your name?: '))
    bid = float(input("What's your bid?: "))
    check_bidders = str(input("Are there any other bidders?: 'yes' or 'no'"))

    auction_bids[bidder_name] = bid

    if check_bidders == 'yes':
        clear()
    else:
        do_auction = False
        check_winner(auction_bids)
