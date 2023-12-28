from random import randint

def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        count = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != x + y:
                    raise ValueError
                score += 1
                break
            except ValueError:
                count += 1
                print("EEE")
                if count >= 3:
                    print(f"{x} + {y} = {x + y}")
                    break
                pass
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level <= 0 or level >= 4:
                raise ValueError
            return level
        except ValueError:
            pass

def generate_integer(level):
    a = 10**(level-1)
    if a == 1:
        a = 0
    return randint(a,10**level-1)


if __name__ == "__main__":
    main()
