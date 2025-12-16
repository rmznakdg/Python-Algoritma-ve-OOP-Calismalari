sayı = int(input("Tam bölenlerini bulmak istediğiniz sayıyı giriniz:"))
i=1
for i in range(1,sayı+1):
    if sayı%i==0:
        print(i,",",sayı,"'sının tam bölenlerinden biridir.")
    else:
        i+=1

