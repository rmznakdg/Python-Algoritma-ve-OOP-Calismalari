while True: #Eğer hiçbir yerde sonlandırma ifadesi kullanılmazsa bu döngü sonsuza kadar devam eder.
    nickname = input("Kullanıcı adınızı giriniz (Çıkış yapmak için 'q' tuşuna basınız):")
    if nickname == "q":
        print("Çıkış yaoıldı.")
        break
    print("Kullanıcı adınız:",nickname)

