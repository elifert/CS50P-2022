from datetime import date
import re, inflect, operator, sys

p = inflect.engine()
time = r"^([1-2]?\d{3})-(0\d|1[0-2])-(0\d|1\d|2\d|3[0-1])$"

class Age:
    def __init__(self, birthday):
        if re.search(time, birthday):
            self.birthday = birthday
        else:
            raise ValueError

    def __str__(self):
        substracted = operator.sub(date.today(), date.fromisoformat(self.birthday))
        return f"{p.number_to_words(round(substracted.total_seconds()/60), andword='').capitalize()} minutes"

def main():
    try:
        print(get_age(input("Date of Birth: ")))
    except ValueError:
        sys.exit("Invalid date")

def get_age(input):
    age = Age(input)
    return age.__str__()

if __name__ == "__main__":
    main()
