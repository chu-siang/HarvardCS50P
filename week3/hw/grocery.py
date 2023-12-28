mp = {}

while True:
    try:
        a = input().upper()
        if a not in mp:
            mp[a] = 0
        mp[a] += 1
    except EOFError:
        break
for Key, Value in sorted(mp.items()):
    print(Value,Key)

