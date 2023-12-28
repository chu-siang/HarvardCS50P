# Yummy Restaurant

#### Video Demo: 👀 : <https://youtu.be/VZX32uQTxVs>

#### Description:
User can order multiple food and drink items
Calculates total bill based on preset prices
Option to not order anything and exit
Fun ASCII art responses using pyfiglet and cowsay
Usage
Run python yummy.py and follow the prompts to order food and drinks.

Say "No Thanks" when prompted to skip ordering that menu item.

The provided Python code represents a simple command-line interface for a fictional restaurant named "Yummy Restaurant." Let's break down the code functionality and structure:

Menu Definitions:

The restaurant offers food and drink menus, each item identified by a number (No.1 to No.5) and represented by emojis.
The cost of each menu item is defined in the check_bill dictionary.
Main Function (main):

Initializes a Figlet object to display a stylized welcome message.
Attempts to read and display the food and beverage menus from CSV files using the tabulate library.
Handles the case where the menu files are not found, exiting the program if so.
Asks the user to input their food and drink preferences, providing instructions for formatting.
Builds a string List to store the selected items.
Food and Drink Selection (foods and drinks functions):

Parses user input for food and drink selections, updating the List string accordingly.
Splits input by commas and then further by asterisks to get the item number and quantity.
Capitalizes and matches the item number with the corresponding emoji from the menus.
Checkout Function (checkout):

Calculates the total bill based on the items in the List using the prices defined in check_bill.
Returns 0 if the list is empty, indicating no order.
Execution (__main__ block):

Invokes the main function when the script is run.


There are two menus - a food menu and a drinks menu:

Foods Menu

No.	Item
1	🍔
2	🥪
3	🍟
4	🥗
5	🌮

Drinks Menu

No.	Item
1	🥤
2	☕
3	🧃
4	🍹
5	🥛

how to implement:
---
First Input the `No.[1-5] * [n], No.[1-5] * [n]`

    No.'Your'foods number' * N 'the numbers of that food you want to eat'
    Ex: No.1 * 2, No.3 * 4
    Please notice we use comma to seperate different foods
If you just want eat a burger you can input like this

    No.1 * 1

Next you can input the drinks number as same as foods

    No.2 * 1
And finally you will get the output!

If you don't want drinks or foods just input

    No Thanks


### And please notice the  `requirement.txt`
---
first need imports following package:

    1.import sys
    2.import csv
    3.from tabulate import tabulate
    4.from pyfiglet import Figlet
    5.import cowsay
Second:

    needs to add instruction in terminal: pip install cowsay
    //which means install the package (cowsay)
Third:

    check the csv file is in the project folder(menu_beverages.csv and menu_foods.csv)
    //which used in project

