nickname = "Ramazan"
parola = "16495ab"

girilennickname = input("Kullancı adınızı giriniz:")
girilenparola = input("Şifrenizi giriniz:")
if nickname == girilennickname and parola != girilenparola :
    print("Parolayı yanlış girdiniz:")
elif nickname != girilennickname and parola == girilenparola :
    print("Kullanıcı adını yanlış girdiniz:")
elif nickname != girilennickname and parola != girilenparola :
    print("Kullanıcı adı ve parolayı yanlış girdiniz:")
else: print("Sisteme hosgeldiniz:")

