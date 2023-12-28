import requests
import json
import sys
try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    a = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    c = response.json()["bpi"]["USD"]["rate_float"]
    print(f"${c*a:,.4f}")
except (ValueError,requests.RequestException):
    sys.exit("Command-line argument is not a number")
