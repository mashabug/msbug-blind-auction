from replit import clear

from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_highests_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Maria": 69, "Jordan": 100}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What's your name?:\n")
  price = int(input("What's your bit?\n$"))
  bids[name] = price
  should_continue = input("Is there other user you want to add?\nType 'yes' or 'no'.\n")
  if should_continue == 'no':
    bidding_finished = True
    find_highests_bidder(bids)
  elif should_continue == 'yes':
    clear()
