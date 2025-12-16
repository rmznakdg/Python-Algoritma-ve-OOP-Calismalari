birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

def yazıyaçevir(sayı):
    if sayı < 10 or sayı > 99:
        return "İki basamaklı bir sayı giriniz"

    ikimci = sayı%10
    birinci = sayı//10
    return onlar[birinci] + birler[ikimci]
sayı =int(input("Sayı:"))
print(yazıyaçevir(sayı))