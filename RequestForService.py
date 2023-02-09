""" Bu uygulama Hakan KOCAMAN tarafından ArcGIS rest servileri üzerinden
boylam ve enlem coğrafi koordinatları kullanılarak ilgili konuma ait adres bilgisini
temin etmek için kodlanmıştır.Çalışma henüz test aşamasındadır. Daha fazla bilgi ve
iletişim için www.hakankocaman.com adresini ziyeret edebilir iletisim@hakankocaman.com
adresine e-posta atabilirsiniz."""

#!/usr/bin/env python
#-*-coding:utf-8-*-

#Sorgu işleminde kullanılacak modüller:
#(eğer modüller yüklü değil ise komut sistemine "pip install requests" komutunu kullanarak yükleyebilirsiniz)
import requests, json

try:
  file=open("coordinate.txt","r+",encoding="utf-8")
  coordinate=file.readlines() 

except FileNotFoundError:
  print("File coordinate.txt not found!")

#Sorgu sonucu listelenecek başlıklar:
print ("IP","Ülke","İl","İlçe","Enlem","Boylam")
#long=-117.205525
#lat=34.038232
#lt=str(long) + "," + str(lat)
#Sorgulanacak ip lere ait liste:
ip = ["176.55.55.252","176.55.55.252","88.230.177.68","88.230.177.68"]
APIKEY = ""
#ip listesinin teker teker web servis üzerinden sorgulanması:
for lonlat in coordinate:
    lt=str(lonlat.replace(" ", ","))
    #print(lt)
    #Bu kısımda yer alan API_KEY'i https://ipstack.com/ adresine üye olarak temin edebilirsiniz.
    serviceURL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?distance=&langCode=&locationType=&featureTypes=&outSR=&returnIntersection=false&f=pjson&location='+lt  
    
    #print(serviceURL)
    r = requests.get(serviceURL)
    y = json.loads(r.text)
    #print(y)
    #print(y["address"],y["location"])
    yy=y["address"]
    print(yy["Address"], ","+lt)
    #print(y["address"],y["country_name"],y["region_name"],y["city"],y["latitude"],y["longitude"]) 