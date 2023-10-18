import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

while True:
    currency = input("What currency(EUR, USD, PLN) do you want to exchange for UAH? To quit(enter 'q'): ")
    if currency == 'q':
        break
    if currency == "EUR" or currency == "USD" or currency == "PLN":
        amount_foreign = input(f"How many {currency} you want to exchange? To quit(enter 'q'): ")
        if amount_foreign == 'q':
            break

        for elem in response.json():
            if elem['cc'] == currency:
                print(f"\nCurrent exchange rate of the {elem['cc']}: {elem['rate']} грн\n \nYou exchanged {amount_foreign} {elem['cc']} for {elem['rate']*float(amount_foreign)} UAH\n")
                break
    else:
        print("You can only exchange EUR, USD pr PLN for UAH")
