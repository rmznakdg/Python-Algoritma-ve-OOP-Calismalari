'''
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

'''

a = int(input("a değerini giriniz:"))
b = int(input("b değerini giriniz:"))
c = int(input("c değerini giriniz:"))

delta = b ** 2 -  4 * a * c
x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)
kökler = [x1,x2]
print("Birinci kök: {}\nİkinci kök:{}".format(kökler[0],kökler[1]))
