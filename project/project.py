import sys
import csv
from tabulate import tabulate
from pyfiglet import Figlet
import cowsay

# Yummy restaurant
drinks_menu = {
    "No.1": "🥤",
    "No.2": "☕",
    "No.3": "🧃",
    "No.4": "🍹",
    "No.5": "🥛"
}

foods_menu = {
    "No.1": "🍔",
    "No.2": "🥪",
    "No.3": "🍟",
    "No.4": "🥗",
    "No.5": "🌮"
}

check_bill = {
    "🍔": 7.5,
    "🥪": 5.0,
    "🍟": 3.5,
    "🥗": 1.5,
    "🌮": 4.5,
    "🥤": 1.5,
    "☕": 2.0,
    "🧃": 2.5,
    "🍹": 2.5,
    "🥛": 2.0,
}


def main():
    figlet = Figlet()
    figlet.setFont(font="standard")
    print(figlet.renderText("Hello! Welcome to Yummy Restaurant.\n"))
    print("Here are the menus:")
    try:
        with open("menu_foods.csv") as file1, open("menu_beverages.csv") as file2:
            print(tabulate(csv.DictReader(file1), headers="keys", tablefmt="grid"))
            print(tabulate(csv.DictReader(file2), headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
    print("\nWhich foods would you like to order? ")
    print("please press foods No. in menu with your keybords: ")
    print("For example: No.1 * 1, No.2 * 3")
    print("If you don't want any foods just say [No Thanks]")
    s = input("Which foods would you like to eat?")
    List = ""
    if s != "No Thanks":
        List += foods(s)
        print(f"here it is: {foods(s)}")
    print("\nDo you want some drinks?")
    print("please press drinks No. in menu with your keybords: ")
    print("for example: No.1 * 1, No.2 * 2")
    print("If you don't want any drinks just say [No Thanks]")
    s1 = input("Which beverages would you like to drink?")
    if s1 != "No Thanks":
        List += drinks(s1)
        print(f"here it is{drinks(s1)}")
    bill = checkout(List)
    if bill == 0:
        cowsay.ghostbusters("You don't have any order")
    else:
        cowsay.cow(f"Here is your meal: {List}")
        cowsay.cow(f"Here is your bill: ${checkout(List)}")


def drinks(drink):
    drink_list = drink.strip().split(",")
    s = ""
    for _ in drink_list:
        no, num = _.strip().split("*")
        no = no.strip().capitalize()
        s += drinks_menu[no]* int(num.strip())
    return s


def foods(food):
    food_list = food.strip().split(",")
    s = ""
    for _ in food_list:
        no, num = _.strip().split("*")
        no = no.strip().capitalize()
        s += foods_menu[no]* int(num.strip())
    return s

def checkout(List):
    num = 0
    if List == "":
        return 0
    for _ in range(len(List)):
        num += check_bill[List[_]]
    return num


if __name__ == "__main__":
    main()
