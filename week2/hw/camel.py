name = input("camelCase: ")
print("snake_case: ",end = "")
for c in name:
    if c.isupper():
        print("_", c.lower(),sep = "",end = "")
    else:
        print(c,end = "")
print()


'''
camel = input("camelCase: ").strip()

snake = "".join(["_" + ch.lower() if ch.isupper() else ch for ch in camel])
print("snake_case:", snake)
'''