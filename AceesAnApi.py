import requests

def name(nae):
   url =f"https://pokeapi.co/api/v2/pokemon/{nae}"
   u = requests.get(url)
   if u.status_code==200:
        h=u.json()
        return h
   else:
        print("Invalid name")  

nae=input("Enter pikachu name")
kiks = name(nae)
if kiks:
    print(kiks["name"])
    print(kiks["id"])

