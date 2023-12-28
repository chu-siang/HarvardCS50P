import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
count = 0
try:
    with open(sys.argv[1],"r") as file:
        for line in file:
            line = line.strip()
            if len(line) > 1 and line[0] != "#" and line[0:3] != "'''" and line[0:3] != '"""':
                count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist.")
