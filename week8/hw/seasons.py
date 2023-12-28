from datetime import date
import inflect
import sys

def get_minutes(bd, today):
    return 60*24*(today - bd).days


def main():
    try:
        bd = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")
    total_minutes = get_minutes(bd, date.today())
    w = inflect.engine()
    print(f"{w.number_to_words(total_minutes, andword='').capitalize()} {w.plural('minute', total_minutes)}")
if __name__ == "__main__":
    main()