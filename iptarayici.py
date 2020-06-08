import requests,json


ip = input("IP ADRESİNİ GİRİNİZ : " + "")
serviceURL = "http://api.ipapi.com/"+ip+"?access_key="+"f76460f4e8673c445e56d09769f54243"+"&output=json"
r = requests.get(serviceURL)
y = json.loads(r.text)
y = json.loads(r.text)
veri = y["latitude"],y["longitude"]
print("İP ADRESİ HAKKINDA BİLGİLER YÜKLENİYOR ...")
print("İP ADRESİ HAKKINDA BİLGİLER YÜKLENİYOR ...")
print("İP ADRESİ HAKKINDA BİLGİLER YÜKLENİYOR ...")
print("İP ADRESİ HAKKINDA BİLGİLER YÜKLENİYOR ...")
print("----------------------------------------------")
print("OTURDUĞU ÜLKE :  " + "" +y["country_name"])
print("OTURDUĞU iL : " + "" +y["region_name"])
print("OTURDUĞU Şehir :  "+ "" +y["city"])
print("KONUM KORDİNATLARI : " + "" + str(veri))
print("----------------------------------------------")
print("20 KM YANILMA PAYI VAR .")