sayı = input("Bir sayı giriniz:")
basamaksayisi = len(sayı)
toplam = 0

for i in sayı:
    x = int(i) ** len(sayı)
    toplam+=x
if toplam==int(sayı):
    print(sayı,"'sayısı armstrong sayısıdır.")
else: print(sayı,"'sayısı armstrong sayısı değildir.")