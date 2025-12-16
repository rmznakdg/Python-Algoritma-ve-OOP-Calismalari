""""
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""
not1 = int(input("1. vize notunuzu giriniz:"))
not2 = int(input("2. vize notunuzu giriniz:"))
final = int(input("1. final notunuzu giriniz:"))
ort = not1*30/100 + not2*30/100 + final*40/100

if ort>=90:
    print("AA")
elif ort>=85:
    print("BA")
elif ort>=80:
    print("BB")
elif ort>=75:
    print("CB")
elif ort>=70:
    print("CC")
elif ort>=65:
    print("DC")
elif ort>=60:
    print("DD")
elif ort>=55:
    print("FD")
elif ort<55:
    print("FF")
else: print("Lütfen geçerli not giriniz:")

