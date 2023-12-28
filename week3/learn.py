'''SyntaxError. ValueError. try. except. NameError. else. pass. raise.'''
while True:
    try:
        x = int(input("What's x ? "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")

'''
def main():
    x = get_int()
    print(f"x is {x}")
    
def get_int():
    while True:
        try:
            return int(input("What's x ? "))
        except ValueError:
            pass
main()
'''