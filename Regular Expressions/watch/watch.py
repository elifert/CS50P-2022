import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match:= re.search(r'^.*"https?://(?:www\.)?youtube\.com/embed(/.+)".*$', s, re.IGNORECASE):
        URL = re.sub("/", "https://youtu.be/", match.group(1))
        return URL
    else:
        return None

if __name__ == "__main__":
    main()