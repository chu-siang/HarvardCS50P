import re

'''re.sub(pattern,repl,string,count=0,flags=0)'''
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Usernam:", matches.group(1))
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "",url)
# print(f"Username: {username}")