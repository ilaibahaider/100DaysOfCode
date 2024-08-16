import art
print(art.logo)

def find_highest(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

auction = {}
continue_bidding = True
while continue_bidding:
    bidder_name = input("What's your name?: ")
    bid_price = int(input("What's your bid? : $"))
    auction[bidder_name] = bid_price
    should_continue = input("Are there others who want to bid? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest(auction)
    elif should_continue == "yes":
        print("\n" * 20)

