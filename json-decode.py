import json

data='[{ "nama" : "Hendrawan" , "alamat" : "Kaligangsa wetan Brebes" },' \
     '{"nama" : "Yanto" , "alamat" : "Tegal"}]'


result = json.loads(data)

for x in result:
    print (x['nama'])