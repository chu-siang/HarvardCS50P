import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.match(r'(\d{1,2})(?::)?(\d{2})? (AM|PM) to (\d{1,2})(?::)?(\d{2})? (AM|PM)',s):
        sh, sm, sap, eh, em, eap = matches.groups()
        if sm is None and em is None:
            sm , em = 0,0
        sh,sm,eh,em = map(int,[sh,sm,eh,em])
        if eap == "PM" and eh != 12:
            eh += 12
        elif eap == "AM" and eh == 12:
            eh = 0
        if sap == "PM" and sh != 12:
            sh += 12
        elif sap == "AM" and sh == 12:
            sh = 0
        if ( not 0 <= sh <= 23 or not 0 <= sm <= 59 or not 0 <= eh <= 23 or not 0 <= em <= 59):
                raise ValueError("Invalid arguments")
        return f"{sh:02d}:{sm:02d} to {eh:02d}:{em:02d}"
    raise ValueError("Invalid arguments")
if __name__ == "__main__":
    main()




