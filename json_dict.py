import json

mahasiswa = []

hendrawan = {"nama" : "Hendrawan" , "alamat" : "Kaligangsa wetan Brebes"}
anto = {"nama" : "Anto" , "alamat" : "Tegal"}
yadi = {"nama" : "Yadi" , "alamat" : "Bulakamba"}

mahasiswa.append(hendrawan)
mahasiswa.append(anto)
mahasiswa.append(yadi)

json_str =json.dumps(mahasiswa)
print (json_str)