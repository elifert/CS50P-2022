months = {
        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
    }

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) > 12 or int(day) > 31:
                raise ValueError
            print(f"{year.strip()}-{int(month):02}-{int(day):02}")
            break
        elif "," in date:
            month_date, year = date.split(", ")
            month, day = month_date.split(" ")
            if int(day) > 31:
                raise ValueError
            print(f"{year}-{months[month]}-{int(day):02}")
            break
    except (ValueError, NameError, KeyError):
        pass