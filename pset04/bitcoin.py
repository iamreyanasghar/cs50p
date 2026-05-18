import requests 
import sys

try:
    n = float(sys.argv[1])

    # replace YOUR_API_KEY with your actual API key on 'https://pro.coincap.io/dashboard'
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY")

    output = response.json()

    usd = float(output['data']['priceUsd'])
    amount = n * usd

    print(f"${amount:,.4f}")


except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")


