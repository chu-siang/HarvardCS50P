from pyfiglet import Figlet
import random
import sys

figlet = Figlet().getFonts()
if len(sys.argv) == 1:
    s = input("Input: ")
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in figlet:
        sys.exit("Invalid usage")
    else:
        try:
            figlet = Figlet()
            figlet.setFont(font = sys.argv[2])
            s = input("Input: ")
            print(figlet.renderText(s))
        except (ValueError):
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
# figlet.setFont(font = f)
