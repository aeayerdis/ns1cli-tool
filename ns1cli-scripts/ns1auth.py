##Create pvar.json (POST Key) and gvar.json (ReadOnly Key) and save to your user home directory or wherever you want
#[
#{
#  "apiKey":"keyID"  
#}
#]

import json

with open('C:/Users/UserName/pvar.json', 'r') as auth:
    p_data = json.load(auth)

for p in p_data:
    pkey = p["apiKey"]

with open('C:/Users/UserName/gvar.json', 'r') as authg:
    g_data = json.load(authg)

for g in g_data:
    gkey = g["apiKey"]


gk = gkey

pk = pkey
