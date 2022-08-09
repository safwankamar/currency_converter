import requests
amount_convert = input('enter amount to convert')
from_currency =  input('enter from which currency to convert ex:INR')
to_currency = input('enter convert to which currency ex:USD')
from_currency=str(from_currency)
to_currency= str(to_currency)


complete_url = "https://api.apilayer.com/fixer/convert?"+"to=" + to_currency + "&from=" + from_currency + "&amount=" + amount_convert
headers = {"apikey": "0DCeev8W6uhxZO6X18LUTU7x6t53FqqP"}
response = requests.get(complete_url,headers=headers)
x = response.json()
converted_amt = x["result"]
otherdata = x["query"]
for key,values in otherdata.items():
        print(f'{key} - {values}')
print(f' converted amount = {amount_convert}{from_currency} = {converted_amt} {to_currency}')
