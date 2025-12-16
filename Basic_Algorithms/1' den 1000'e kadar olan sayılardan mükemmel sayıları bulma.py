sayı = int(input("Bir sayı giriniz:"))
toplam = 0
if sayı > 1 and sayı < 1000:
    for i in range(1,sayı):
        if sayı%i==0:
            toplam+=i
    if sayı == toplam:
        print("Bu sayı bir mükemmel sayıdır.")
    else: print("Bu sayı mükemmel bir sayı değildir.")
else: print("Lütfen 1 ile 1000 arasında bulunan bir sayı giriniz.")
    

