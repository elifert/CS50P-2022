import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        number1, number2 = generate_integer(level)
        sum = number1 + number2
        for a in range(3):
            print(f"{number1} + {number2} = ", end="")
            try:
                guess = int(input())
                if guess == sum:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                continue
            if a==2:
                print(f"{number1} + {number2} = {number1 + number2}")
    print("Score: ", score)
        
def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if 1<=x<=3:
                return x
        except (ValueError, TypeError):
            pass
    
def generate_integer(level):
    starting = 40*(level**2) - 110*level + 70
    ending = 10**level - 1
    number1 = random.randint(starting, ending)
    number2 = random.randint(starting, ending)
    return number1, number2

if __name__ == "__main__":
    main()