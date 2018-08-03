import requests;


def getExchangeRate(currency):
    file = requests.get("http://data.fixer.io/api/latest?access_key=b96a72bed66245c7dff0d19efb83b1ee")
    data = file.json();
    try:
        return data['rates'][currency];
    except:
        print("Currency not found. It will be charged in Euros");
        return 1;
