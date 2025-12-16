def asalmi(sayı):
    sayı = int(sayı)  # Gelen girişi tamsayıya dönüştür
    if sayı == 1:
        return False
    elif sayı == 2:
        return True
    else:
        for i in range(2, int(sayı)): 
            if sayı % i == 0:
                return False
        return True

while True:
    sayı = input("Asal sayı mı merak ettiğiniz sayıyı giriniz:")
    if sayı.lower() == "k":
        print("Program sonlandırılıyor.")
        break
    else:
        if sayı.isdigit():  # Girilen değerin bir sayı olduğunu kontrol et
            if asalmi(sayı):
                print("Bu sayı asal sayıdır.")
            else:
                print("Bu sayı asal sayı değildir.")
        else:
            print("Lütfen bir tamsayı girin.")

        