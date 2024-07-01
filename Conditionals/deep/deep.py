smth = input()
match smth:
    case "42" | "forty two" | "forty-two" | "Forty two" | "Forty-two" :
        print("Yes")
    case _:
        print("No")