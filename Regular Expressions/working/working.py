import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = r"(0?[0-9]|1[0-9]|2[0-3]):?([0-5][0-9])? (AM|PM)?"
    if match := re.search(f"^{time} to {time}$", s):
        return f"{arrange(match[1], match[2], match[3])} to {arrange(match[4], match[5], match[6])}"
    else:
        raise ValueError

def arrange(x, y, z):
    if y is None:
        y = 0
    if int(x) != 12:
        match z:
            case "AM":
                return f"{int(x):02}:{int(y):02}"
            case "PM":
                return f"{(int(x)+12):02}:{int(y):02}"
    else:
        match z:
            case "AM":
                return f"00:{int(y):02}"
            case "PM":
                return f"{(int(x)):02}:{int(y):02}"

if __name__ == "__main__":
    main()