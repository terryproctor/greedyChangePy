quarters = 0
dimes = 0
nickels = 0
pennies = 0

#asks pax for change in cents until a value is more than 0 (gets rid of negative values)
while True:
    change = float(input("How much change do you need in dollars?\t"))
    change_needed = change * 100
    change_needed = int(change_needed)
    if change_needed > 0:
        break
    else:
        continue

if change_needed >= 25:
    quarters_given = change_needed // 25
    quarters += quarters_given
    change_needed = change_needed - (quarters_given * 25)

if change_needed >= 10:
    dimes_given = change_needed // 10
    dimes += dimes_given
    change_needed = change_needed - (dimes_given * 10)

if change_needed >= 5:
    nickels_given = change_needed // 5
    nickels += nickels_given
    change_needed = change_needed - (nickels_given * 5)

pennies_given = change_needed
pennies += pennies_given

print(f"Change to give: {change}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")