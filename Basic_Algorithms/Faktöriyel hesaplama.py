

print("""
*************************
Faktörüyel Bulma Programı

Çıkmak için q tuşuna basınız.
*****************************""")
while True:
    sayı = input("Faktöriyelini merak ettiğiniz sayıyı giriniz:")
    çarpım = 1
    if sayı=="q":
        print("Program Sonlandırılmıştır.")
        break
    sayı = int(sayı)
    for i in range(1,1+sayı):
        çarpım*=i
    print(çarpım)


