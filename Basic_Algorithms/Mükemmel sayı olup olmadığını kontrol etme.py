
'''
toplam = 0
sayı = int(input("Bir sayı giriniz:"))
for i in range(1,sayı):
    if sayı % i ==0:
        toplam+=i
if toplam==sayı:
    print("Bu sayı mükemmel bir sayıdır.")
else: print("Bu sayı mükemmel bir sayı değildir.")
'''
sayı = int(input("Bir sayı giriniz:"))
toplam = 0
i=1
while i < sayı:
    if (sayı % i == 0):
        toplam+=i
    i+=1
if sayı == toplam:
    print("Bu sayı mükemmel bir sayıdır.")
else: print("Bu sayı mükemmel bir sayı değildir.")        