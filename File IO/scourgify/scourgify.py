import csv
import sys

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else: 
    try:
        file1 = open(sys.argv[1])
        with open(sys.argv[2], "w") as file2:
            read_file1 = csv.DictReader(file1)
            writer_file2 = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer_file2.writeheader()
            for row in read_file1:
                last, first = row["name"].split(",")
                writer_file2.writerow({"first": first.lstrip(), "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")