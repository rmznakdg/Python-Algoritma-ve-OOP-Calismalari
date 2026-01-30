from datetime import datetime
print("""
Günlük programına hoşgeldiniz..
Yazılan tüm yazıları görmek için 'oku' yazınız.
Programdan çıkmak için ise 'çık' yazınız.
""")
while True:
    metin = input("Bugün ne yazmak istiyorsunuz?:")
    zaman = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if metin == "oku":
        with open("Günlük Programı.txt","r",encoding="utf-8") as file2:
            print(file2.read())
    elif metin == "çık":
        print("Program sonlandırılıyor, bugünlük bu kadardı")
        break
    else:
        with open("Günlük Programı.txt","a", encoding = "utf-8") as file:
            file.write(f"[{zaman}]:,{metin}\n")
