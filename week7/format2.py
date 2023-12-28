import re
name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$",name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
    #method 1
    # last, first = matches.groups()
    # name = f"{first}, {last}"
    #method 2
    # last = matches.group(1)
    # first  = matches.group(2)
    # name = f"{first} {last}"

print(f"hello, {name}")
