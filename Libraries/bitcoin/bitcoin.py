import sys
import requests

if len(sys.argv)==1:
    sys.exit("Missing command-line argument")
else:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
link = response.json()

usd_rate = link["bpi"]["USD"]["rate_float"]
bitcoin_price = usd_rate * amount
print(f"${bitcoin_price:,.4f}")