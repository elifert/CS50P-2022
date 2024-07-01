name = input("camelCase: ")
print("snake_case: ", end="")
for s in name:
    if s.isupper():
        print(f"_{s.lower()}", sep="", end="")
    else:
        print(s, sep="", end="")