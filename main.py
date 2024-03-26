is_continue = True
auction = []
while is_continue:
    name = input("Enter your Name: ")
    bid_price = float(input("Enter bid price: "))
    auction.append({name: bid_price})
    answer = input("Any Other who want to bid: ").lower()
    if answer == 'no':
        is_continue = False

highest_bid = float('-inf')
highest_bidder = None

for entry in auction:
    for name, price in entry.items():
        if price > highest_bid:
            highest_bid = price
            highest_bidder = name

if highest_bidder is not None:
    print(f"The Winner is {highest_bidder} and the bid is {int(highest_bid)}")
