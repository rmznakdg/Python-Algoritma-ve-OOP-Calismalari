"""
Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""
kilo = float(input("Kilonuzu kg cinsinden giriniz:"))
boy = float(input("Boyunuzu  m cinsinden giriniz:"))
bki = kilo / (boy*boy)
if bki<18.5:
    print("Zayıf")
elif bki>=18.5 and bki<25:
    print("Normal")
elif bki>=25 and bki<30:
    print("Fazla kilolu")
else: print("Obez")
