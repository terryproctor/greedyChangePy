notes_and_coins = [1000,500,200,100,50,25,10,5,1]
notes_and_coins.sort(reverse=True)
coins = 0

#asks pax for change in cents until a value is more than 0 (gets rid of negative values)
while True:
    change = float(input("How much change do you need in dollars?\t"))
    change_needed = change * 100
    change_needed = int(change_needed)
    if change_needed > 0:
        break
    else:
        continue

#check every coin and note in array
for i in range(len(notes_and_coins)):
    if change_needed >= notes_and_coins[i]:
        coins += change_needed // notes_and_coins[i]
        change_needed %= notes_and_coins[i]
    else:
        continue

#print results    
print(f"Change to give: {change}")
print(f"Coins to give: {coins}")