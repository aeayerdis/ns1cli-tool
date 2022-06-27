import json

with open('C:/Users/Aaron.Ayerdis/pvar.json', 'r') as auth:
    p_data = json.load(auth)

for p in p_data:
    pkey = p["apiKey"]

with open('C:/Users/Aaron.Ayerdis/gvar.json', 'r') as authg:
    g_data = json.load(authg)

for g in g_data:
    gkey = g["apiKey"]


gk = gkey

pk = pkey
