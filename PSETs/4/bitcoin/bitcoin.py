import requests
import sys

key: str="API_KEY"
api: str= f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={key}"

try:
    btc = float(input("Bitcoins: "))
    request: object = requests.get(api)
    price_usd = float(request.json()["data"]["priceUsd"])
    total_cost = round(price_usd*btc, 2)

    print(f"{btc} bitcoins are worth ${total_cost:,}")
except requests.RequestException:
    print("Hello")
except ValueError:
    sys.exit("Invalid number of bitcoins")