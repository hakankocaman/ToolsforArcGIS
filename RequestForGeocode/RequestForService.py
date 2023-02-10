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

  file2=open("adress.txt","w",encoding="utf-8")
  file2.close()
except FileNotFoundError:
  print("File coordinate.txt not found!")


#koordinat listesinin teker teker web servis üzerinden sorgulanması:
for lonlat in coordinate:
  lt=str(lonlat.replace(" ", ","))

  serviceURL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?distance=&langCode=&locationType=&featureTypes=&outSR=&returnIntersection=false&f=pjson&location='+lt  
    
  #print(serviceURL)
  r = requests.get(serviceURL)
  y = json.loads(r.text)

  yy=y["address"]
  if yy["Address"]=="":
    yy["Address"]="Adress not found!"

  #print(yy["Address"], ", "+lt)

  c=yy["Address"], ", "+lt

  c=str(c)
  file2=open("adress.txt","a+",encoding="utf-8")
  file2.write(c+"\n")
file2.close()
print("işlem tamamlandı")
