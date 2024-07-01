def main():
    smth = input().strip()
    greetings(smth)

def greetings(n):
    if 'hello' in n.lower():
        print("$0")
    elif n.startswith(('h', 'H')):
        print("$20")
    else:
        print("$100")

main()