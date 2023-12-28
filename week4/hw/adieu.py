import inflect


p = inflect.engine()
lst = []
while True:
    try:
        lst.append(input("Name: ").strip())
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(lst)}")
