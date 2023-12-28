def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    a = "aeiouAEIOU"
    for i in a :
        word = word.replace(i,"")
    return f"{word}"


if __name__ == "__main__":
    main()





# s = input("Input: ")
# s2 = "".join(c for c in s if c not in "aeiouAEIOU")
# print("Output:",s2)
