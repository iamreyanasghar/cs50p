amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted in [25, 10, 5]:
        amount_due -= coin_inserted
        continue
    else:
        print(f"Amount_due: {amount_due}")


change = abs(amount_due)
print(f"Change Owed: {change}")
