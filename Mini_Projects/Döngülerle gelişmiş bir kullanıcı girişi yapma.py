print("""
*************************
Kullanıcı Girişi Programı
*************************""")

isim = "ramazann1"
parola = "123689"
kalanhak = 3
while True:
    girilenisim = input("Kullanıcı adınızı giriniz:")
    girilenparola = input("Kullanıcı adınızı giriniz:")
    if (girilenisim ==  isim and girilenparola != parola):
        print("Parola Hatalı!")
        kalanhak-=1
        print("(İyice düşünün!) Kalan giriş hakkı:",kalanhak)
    elif (girilenisim !=  isim and girilenparola != parola):
        print("Kullanıcı Adı ve Parola Hatalı!")
        kalanhak-=1
        print("(İyice düşünün!) Kalan giriş hakkı:",kalanhak)
    elif (girilenisim !=  isim and girilenparola == parola):
        print("Kullanıcı Adı Hatalı!")
        kalanhak-=1
        print("(İyice düşünün!) Kalan giriş hakkı:",kalanhak)
    else:
        print("Sisteme giriş yapılıyor...")
        break
    if (kalanhak == 0):
        print("Hesabınız Bloke Oldu.")
        break





