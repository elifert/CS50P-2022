letters = ['a', 'e', 'i', 'o', 'A', 'E', 'I', 'O']
x = input("Input: ")

result = ''.join(char for char in x if char not in letters)

print(result)
