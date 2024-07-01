import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    regex = "([0-1]?([0-9]?){2}|2[0-4][0-9]|25[0-5])"
    return True if re.search(fr"^{regex}\.{regex}\.{regex}\.{regex}$", ip) else False
        
if __name__ == "__main__":
    main()