import csv
import tabulate
import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            read_file = csv.reader(file)
            table = tabulate.tabulate(read_file, headers="firstrow", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")
