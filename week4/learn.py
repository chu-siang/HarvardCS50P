"""random. import. from. statistics. Command-Line Arguments. sys. sys.argv. IndexError. sys.exit. Slices. Packages. PyPI. pip. cowsay. APIs. requests. JSON. __name__."""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

"""[1:] 輸出到結尾"""
"""[1:-1]輸出到結尾-1"""
for arg in sys.argv[1:-1]:
    print("Hello my name is", arg)

# import statistics

# print(statistics.mean([100,90]))


# import sys

# try :
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")


# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello my name is", sys.argv[1])
