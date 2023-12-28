def main():
    time = input("What time is it? ")
    cmp = convert(time)
    if 7.0 <= cmp <= 8.0:
        print("breakfast time")
    elif 12.0 <= cmp <= 13.0:
        print("lunch time")
    elif 18.0 <= cmp <= 19.0:
        print("dinner time")
    else:
        print("Your program should output nothing.")

def convert(time):
    hour,miniute = time.split(":")
    hour= float(hour) + float(miniute)/60.0
    return hour


if __name__ == "__main__":
    main()
