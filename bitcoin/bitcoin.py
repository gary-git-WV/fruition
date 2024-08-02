''' Use coindesk API to get current price of bitcoin,
calculate and print out cost of (input) number of
bitcoins'''
import json
import requests
import sys

def main():
    # Get number of bitcoins to buy
    try:
        n = (sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    # verify it's a valid number
    try:
        n = float(n)
    except (TypeError, ValueError):
        sys.exit("Command-line argument is not a number")
    # ping coindesk for current price info
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestsException:
        print("Requests Exception occurred")
    # calculate and print the total cost for purchase
    object = response.json()
    rate = (object["bpi"]["USD"]["rate_float"])
    print(f"${rate * n:,.4f}")

if __name__ == "__main__":
    main()
