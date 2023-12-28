fruit = {
    "apple" : 130,
    "avocado" : 50,
    "bananaa" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon": 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "oranne" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

s = input("Item: ").lower()
if s in fruit:
    print(f"Calories: {fruit[s]}")
