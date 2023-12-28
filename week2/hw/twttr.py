text = input("Input: ")
a = "aeiouAEIOU"
for i in a :
    text = text.replace(i,"")
print("Output:",text)


# s = input("Input: ")
# s2 = "".join(c for c in s if c not in "aeiouAEIOU")
# print("Output:",s2)
