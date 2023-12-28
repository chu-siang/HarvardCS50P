def main():
    c = get_percent()*100
    if c <= 1:
        print("E")
    elif c >= 99:
        print("F")
    else :
        print(f"{c:.0f}","%",sep="")
def get_percent():
    while True:
        try:
            x,y = map(int,input("Fraction: : ").split("/"))
            if y == 0 or x > y:
                continue
            c = float(x/y)
            return c
        except (ValueError,ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
