import re
name = input("What's your name? ").strip()

''':= means if and only if'''
if matches := re.search(r"^(.+), *(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
