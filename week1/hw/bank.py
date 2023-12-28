s = input("Greeting: ").lower()
if s[0:5] == "hello":
    print("$0")
elif s[0] == "h":
    print("$20")
else:
    print("$100")

'''
s = input("Greeting: ").strip().lower()

if s.startswith("hello"):
    print("$0")
elif s.startswith("h"):
    print("$20")
else:
    print("$100")
'''