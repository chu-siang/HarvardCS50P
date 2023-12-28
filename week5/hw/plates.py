def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    elif not all(c.isalnum() for c in s):
        return False
    a = False

    for ch in s:
        if ch.isalpha() and a:
            return False
        elif ch.isdigit() and not a:
            if ch == '0':
                return False
            a = True
    return True

if __name__ == "__main__":
    main()
