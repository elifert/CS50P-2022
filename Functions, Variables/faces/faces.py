def main():
    smth = input()
    convert(smth)

def convert(n):
        if ':)' in n:
            n = n.replace(":)", "🙂")
        if ':(' in n:
            n = n.replace(":(", "🙁")
        print(n)

main()
