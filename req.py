import requests
# YOUR_API_KEY = "3dbdb961c9b01e123d93e31c5ac9435a"
# r =  requests.get("https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey="+ YOUR_API_KEY)
# # print(r.text)
# print(r.status_code)


url = "www.something.com"

data = {
    "p1":4,
    "p2":8
}

r2 = requests.post(url=url,data=data)
print(r2.text)
print(r2.status_code)