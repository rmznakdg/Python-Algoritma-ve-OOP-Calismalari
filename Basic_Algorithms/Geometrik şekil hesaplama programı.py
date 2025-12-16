soru = input("Üçgenin mi dörtgenin mi tipini bulmak istersiniz?")
if soru == "Dörtgen" or "dörtgen" or "DÖRTGEN":
    kenar1 = int(input("Dörtgenin 1. kenarının uzunluğunu giriniz"))
    kenar2 = int(input("Dörtgenin 2. kenarının uzunluğunu giriniz"))
    kenar3 = int(input("Dörtgenin 3. kenarının uzunluğunu giriniz"))
    kenar4 = int(input("Dörtgenin 4. kenarının uzunluğunu giriniz"))
    if kenar4==kenar3 and kenar4==kenar2 and kenar4==kenar1:
        print("Bu dörtgen bir karedir!")
    elif kenar4==kenar3 or kenar4==kenar2 or kenar4==kenar1 or kenar3==kenar2 or kenar3==kenar1 or kenar2==kenar1:
        print("Bu dörtgen bir dikdörtgendir!")
    else: print("Bu dörtgen sıradan bir dörtgendir!")
else: soru == "Üçgen" or "ÜÇGEN" or "üçgen"
    kenar_1 = int(input("Üçgenin 1. kenarının uzunluğunu giriniz"))
    kenar_2 = int(input("Üçgenin 2. kenarının uzunluğunu giriniz"))
    kenar_3 = int(input("Üçgenin 3. kenarının uzunluğunu giriniz"))
    if (kenar_1 >= abs(kenar_3 - kenar_2) and kenar_3 + kenar_2 >=kenar_1) or (kenar_2 >= abs(kenar_3 - kenar_1) and kenar_3 + kenar_1 >=kenar_2) or (kenar_3 >= abs(kenar_1 - kenar_2) and kenar_1 + kenar_2 >=kenar_3):
        if (kenar_2==kenar_3 and kenar_2!=kenar_1) or (kenar_1==kenar_3 and kenar_1!=kenar_2) or (kenar_2==kenar_1 and kenar_2!=kenar_3):
            print("Bu üçgen ikizkenar bir üçgendir.")
        elif kenar_1==kenar_3==kenar_2:
            print("Bu üçgen eşkenar bir üçgendir.")
        else: print("Bu üçgen çeşitkenar bir üçgendir.")
    else: print("Bu üçgen üçgen olma kurallarına uymamktadır.")

