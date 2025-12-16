sayi1 = int(input("1. sayıyı giriniz:"))
sayi2 = int(input("2. sayıyı giriniz:"))
sayi3 = int(input("3. sayıyı giriniz:"))

if sayi1 > sayi2 and sayi1 > sayi3:
    if sayi2 > sayi3:
        print("sayi1>sayi2>sayi3")
    else: print("sayi1>sayi3>sayi2")
elif sayi2 > sayi1 and sayi2 > sayi3:
    if sayi1 > sayi3:
        print("sayi2>sayi1>sayi3")
    else: print("sayi2>sayi3>sayi1")
elif sayi3 > sayi1 and sayi3 > sayi2:
    if sayi1 > sayi2:
        print("sayi3>sayi1>sayi2")
else: print("sayi3>sayi2>sayi1")


