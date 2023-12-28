def main():
    s = input("Fraction: ")
    c = convert(s)*100
    gauge(c)
    print(gauge(c))

def convert(fraction):
    while True:
        try:
            x,y = map(int,fraction.split("/"))
            if x > y:
                raise ValueError
            c = float(x/y)*100
            return c
        except (ValueError,ZeroDivisionError):
            pass
def gauge(c):
    if c <= 1:
        return "E"
    elif c >= 99:
        return "F"
    else :
        return f"{c:.0f}%"
if __name__ == "__main__":
    main()
