initial = 50
sum = 0
while True:
    print("Amount Due: ", initial - sum)
    x = int(input("Insert Coin: "))
    sum += x
    if sum>=50:
        print("Change Owed: ", sum - initial)
        break