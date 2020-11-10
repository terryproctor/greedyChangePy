notes_and_coins_us = [1000,500,200,100,50,25,10,5,1]
notes_and_coins_uk = [1,2,5,10,20,50,100,200,500,1000,2000,5000]
notes_and_coins = []

coins = 0

def which_currency():
    while True:
        currency = input("Which currency dollars or pounds?\t")
        currency = currency.lower()
        if currency == "pounds" or currency == "dollars":
            return currency
        else:
            continue

currency = which_currency()
if  currency == "dollars":
    notes_and_coins = notes_and_coins_us
elif currency == "pounds":
    notes_and_coins = notes_and_coins_uk    
notes_and_coins.sort(reverse=True)

#asks pax for change in cents until a value is more than 0 (gets rid of negative values)
def check_change():
    global change
    while True:
        try:    
            change = float(input(f"How much change do you need in {currency}?\t"))
        except ValueError:
            print("This is not a valid number")
            continue
        change_needed = change * 100
        change_needed = int(change_needed)
        if change_needed > 0:
            return change_needed, change
        else:
            continue

#check every coin and note in array
def check_coins_and_notes(notes_and_coins, change_needed):
    for i in range(len(notes_and_coins)):
        if change_needed >= notes_and_coins[i]:
            global coins
            coins += change_needed // notes_and_coins[i]
            change_needed %= notes_and_coins[i]
        else:
            continue
    return coins

#print results

checking = check_change()
check_coins_and_notes(notes_and_coins, change_needed = checking[0])
print(f"Change to give: {change}")
print(f"Coins to give: {coins}")