x = int(input("İlk tamsayıyı giriniz:"))
y = int(input("İkinci tamsayıyı giriniz:"))
print("Değiştirilmeden önceki değerleri:{}-{}".format(x,y))
x,y = y,x
print("Değiştirildikten sonraki değerleri:{}-{}".format(x,y))
