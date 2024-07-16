import requests
import json


city=input('enter the name of the city:\n')
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
print('''chose 1->for  having full detail of weather
      chose 2-> for temperature only''')
# print(r.text)
# wdic=json.loads(r.text)
n=int(input('enter your desired option:'))
match n:
    case 1:
        print(r.text)
    case 2:
        wdic = json.loads(r.text)
        print(wdic["current"]["temp_c"],'`c')
    case _:
        print('fill correctly')

