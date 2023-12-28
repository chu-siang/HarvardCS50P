s = input("File name: ").lower()
if "jpg" in s or "jpeg" in s:
    print("image/jpeg")
elif "gif" in s:
    print("image/gif")
elif "png" in s:
    print("image/png")
elif "pdf" in s:
    print("application/pdf")
elif "txt" in s:
    print("text/plain")
elif "zip" in s:
    print("application/zip")
else:
    print("application/octet-stream")


'''
types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

s = input("File name: ").strip().lower().split(".")[-1]
print(types.get(s, "application/octet-stream"))
'''