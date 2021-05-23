from logo import logo
print(logo)
def higuest_bid(bids_recods):
    highest = 0
    winner =""
    for bidder in bids_recods:
        bid_amount = bids_recods[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"El ganador es {winner} con {highest}")

bids = {}
bidding =False

while not bidding:
    name=input('Ingrese un nombre: ')
    bid=int(input('Ingrese un nombre: '))
    bids[name] = bid
    continue_bid = input("'yes' o 'no'")
    if continue_bid == 'no':
        bidding = True
        higuest_bid(bids)
    elif continue_bid == 'yes':
        print('ingrese otro usuario')

