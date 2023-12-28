import sys
from PIL import Image,ImageOps


if len(sys.argv) > 3:
    print("Too many command-line arugments")
elif len(sys.argv) < 3:
    print("Too few command-line arguments")

Type = (".jpg",".png",".jpeg")
Input = sys.argv[1]
Output = sys.argv[2]

if ( not Input.endswith(Type) or
    not Output.endswith(Type) or
    Input.split(".")[1] != Output.split(".")[1]):
    sys.exit("Invalid input")
shirt = Image.open("shirt.png")
try:
    with Image.open(Input) as im:
        im = ImageOps.fit(im, shirt.size)
        im.paste(shirt,shirt)
        im.save(Output)
except FileNotFoundError:
    sys.exit("File does not exist.")
