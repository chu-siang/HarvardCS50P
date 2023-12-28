a = 50
while True:
    c = int(input("Insert coin:"))
    if c != 25 and c != 5 and c != 10:
        print(f"Amount Due: {a}")
        continue
    a -= c
    if a <= 0:
        print(f"Change Owed: {abs(a)}")
        break
    else :
        print(f"Amount Due: {a}")
