import re
email = input("What's your email? ").strip()
'''
.   any character except a newline 
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
[^] any character except the sign
[] any character in the bracket
\w : word character (as well as numbers and the underscore)
\W : not a word character
\d :decimal digit
\D :not a decimal digit
\s : whitespace characters
\S : not a whitespace character
A|B either A or B
(....) a group
(?:...) non-capturing version
re.IGNORECASE
re.MULTILINE
re.DOTALL
re.match(pattern,string,flags = 0)
re.fullmatch(pattern,string,flags = 0)
'''
'''if re.search("..*%@..*,email) '''
'''if re.search(r"^.+@.+\.edu$",email)'''
'''if re.search(r"^[^@]+@[^@]+\.edu$",email):'''
'''re.search(r"^\w+@\w+\.(edu|com|gov)$",email)'''
'''re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE)'''
'''re.search(r"^[a-z0-9_ \.]+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE)'''
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("valid")
else:
    print("Invalid")