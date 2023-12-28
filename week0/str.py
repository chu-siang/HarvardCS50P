# use  '+' the string will stick behind the further string without a blank
# use ',' the string between the string u want to print will come with a blank
# use "end" means a keyword of the endline what you want to change ex : end = "???"
# use "sep" means a keyword of the answer you want to print and can seprate the string whatever u want
# ex : sep = "???"
# escape word '\' or use "" to contain '   or use '' to contain "
# special string
# ex : print(f"i want print {name}")
# remove whitespace from str (head and tail): str.strip()
# capitalize : str.capitalize()
# title : str.title
#print("hello \"i want print' this")
#print('"i wnat print this')
name = input("What's your name? ").strip().title()

name = name.strip()
#print("hello," , name , sep= "???",end = "ok\n")
print(f"i want print {name}")

