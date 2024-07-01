import sys

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if ".py" in sys.argv[1]:
        try:
            with open(sys.argv[1]) as python_file:
                code_lines_count = 0
                for line in python_file:
                    line_lstripped = line.lstrip()
                    if line_lstripped and not line_lstripped.startswith('# '):
                        code_lines_count += 1
                print(code_lines_count)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
