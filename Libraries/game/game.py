import random

while True:
    try:
        n = int(input("Level: "))
        break
    except ValueError:
        continue

number_to_guess = random.randint(1,n)
x = int(input("Guess: "))
while x!=number_to_guess:
    if x<number_to_guess:
        print("Too small!")
        x = int(input("Guess: "))
    elif x>number_to_guess:
        print("Too large")
        x = int(input("Guess: "))

print("Just right!")