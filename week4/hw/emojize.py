import emoji

s = input("Input: ")
print("Output: ",end="",sep="")
print(emoji.emojize(s,language = "alias"))
