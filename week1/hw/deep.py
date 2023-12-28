s = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip(",%.")
if "42" in s or "forty-two" in s or "forty two" in s:
    print("Yes")
else:
    print("No")
